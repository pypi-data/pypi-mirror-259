"""
Make a tour with IP cam and send snapshots to a server.
"""

import datetime
import logging
import os
import threading
import typing as t

from crontab import CronSlices, CronTab
from onvif import ONVIFCamera
from uun_iot import EventRegister, Module
from uun_iot.utils import get_iso_timestamp
from uun_livecam.camera import SnapSequence, create_camera, reboot_camera

logger = logging.getLogger(__name__)

# wsdl path relative to this file located in 'modules/SnapCam.py'
# wsdl data will be stored in package folder together with .py files
wsdl_path = os.path.abspath(os.path.dirname(__file__)) + "/../wsdl"


def register_snapcam(ev: EventRegister):
    class SnapCam(Module):
        id = "snapCam"

        def __init__(self, config, uucmd):
            super().__init__(config=config, uucmd=uucmd)

            # store dynamic objects in format {cam_id: (ONVIFCamera instance, SnapSequence instance)}
            self._cameras = {}
            self._init_cameras()
            self._set_crontabs()

            # indicate whether there is a tour in progress, so that it is not interrupted by another tour
            self._tour_lock = threading.Lock()

            # indicate whether there is an (configuration) update in progress to prevent waiting in queue and updating multiple times
            self._update_lock = threading.Lock()

        def _init_cameras(self) -> bool:
            """Initialize all camera objects.
            If all were initialized successfuly, return True. If one or more inits failed, return False.
            """
            all_ok = True
            for cid in self._c():
                self._cameras[cid] = self._create_cam_entry(cid)
                if self._cameras[cid] is None:
                    all_ok = False

            return all_ok

        def _create_cam_entry(
            self, cid: str
        ) -> t.Union[None, t.Tuple[ONVIFCamera, SnapSequence]]:
            """
            Attempt to create a tuple (ONVIFCamera instance, SnapSequence instance) corresponding
            to camera with ID 'cid'.

            Args:
                cid: camera ID

            Returns:
                None if initialization failed, otherwise initialized tuple
            """
            cam = self._c(cid)
            try:
                ip = cam["onvif"]["ip"]
                port = cam["onvif"]["port"]
                user = cam["onvif"]["user"]
                password = cam["onvif"]["password"]
                wsdl = wsdl_path
                positions = cam["tour"]

                camera_obj = create_camera(ip, port, user, password, wsdl)
                camera_entry = (
                    camera_obj,
                    SnapSequence(camera_obj, user, password, positions),
                )
            except Exception as e:
                logger.warning("Exception occured when initializing camera [%s].", cid)
                logger.debug("Exception: %s", e)
                return None

            return camera_entry

        def _get_cam_entry(
            self, cid: str
        ) -> t.Union[None, t.Tuple[ONVIFCamera, SnapSequence]]:
            """
            Ensure that camera with ID 'cid' is properly initialized.
            If it is not initialized, attempt to initialize it.

            Args:
                cid: camera ID

            Returns:
                If the camera was initialized, return the instance.
                Otherwise, return None.
            """
            if cid not in self._cameras:
                raise ValueError(
                    "Camera with ID '{cid}' is not present in configuration."
                )

            if self._cameras[cid] is None:
                logger.debug("Trying to reiinit camera `%s`...", cid)
                cam_entry = self._create_cam_entry(cid)
                if cam_entry:
                    logger.debug("Reiinitialization of camera `%s` done.", cid)
                    return cam_entry
                logger.warning("Reiinitialization of camera `%s` failed.", cid)
                return None

            return self._cameras[cid]

        @ev.on("tick")
        def start_cam_tour(self):
            """
            Make every camera take a predefined tour and send images after each snapshot.
            """

            if self._tour_lock.locked():
                logger.warning(
                    "Tour is already in progress. wait until tours for all cameras are"
                    " finished."
                )
                return

            with self._tour_lock:
                # async loop over all cameras (join all threads in the end)
                # send images as async callback after completing the snapshot
                threads = []
                for cam_id in self._cameras:
                    cam_entry = self._get_cam_entry(cam_id)
                    if cam_entry is None:
                        continue

                    def on_snapshot_get(image_bin, position):
                        timestamp = get_iso_timestamp(
                            datetime.datetime.now(datetime.timezone.utc)
                        )
                        self._send_data((cam_id, timestamp, image_bin, position))

                    _, snap_seq = cam_entry
                    t = threading.Thread(
                        target=snap_seq.loop, kwargs={"callback": on_snapshot_get}
                    )
                    t.start()
                    threads.append(t)

                # wait for all cameras to finish their tours
                for t in threads:
                    t.join()

        @ev.on("external", "reboot")
        def reboot_cam(self, msg: t.Tuple[str, str]) -> str:
            """Reboot camera."""
            _, cam_id = msg
            cam_entry = self._get_cam_entry(cam_id)
            if cam_entry is None:
                logger.warning(
                    "Reboot of camera '%s' failed as it could not be initialized."
                )
                return "fail: camera not initialized"

            cam_obj, _ = cam_entry
            reboot_camera(cam_obj)
            logger.warning("Reboot of camera '%s' successful.", cam_id)
            return "ok"

        def _get_comment(self, cid: str):
            return "reboot camera #cid"

        def _set_crontabs(self):
            with CronTab(user=True) as cron:
                for cid, conf in self._c().items():
                    if not "reboot" in conf or not "cronString" in conf["reboot"]:
                        cron.remove_all(comment=self._get_comment(cid))
                        continue

                    cron_str = conf["reboot"]["cronString"]
                    if not CronSlices.is_valid(cron_str):
                        logger.error("Crontab '%s' is not valid!", cron_str)
                        continue

                    exe = os.path.expanduser("~/.local/bin/uun-livecam")
                    # reboot || (start main app & sleep && reboot)
                    cmd = (
                        f"{exe} reboot {cid} ||(systemctl --user restart uun-livecam &"
                        f" sleep 60 && {exe} reboot {cid})"
                    )

                    job = None
                    for j in cron.find_comment(self._get_comment(cid)):
                        job = j
                    if job is None:
                        job = cron.new(command=cmd, comment=self._get_comment(cid))
                    else:
                        job.set_command(cmd)
                    job.setall(cron_str)

            print(CronTab(user=True).lines)

        @ev.on("update")
        def config_update(self):
            """Reinitialize cameras with new configuration."""

            # prevent waiting in queue and then updating multiple times
            # in case update triggers multiple times during a tour
            if self._update_lock.locked():
                return

            with self._update_lock:
                with self._tour_lock:
                    # wait to finish all tours (do not decontruct object for active cameras)

                    # reinitialize cameras with new config (no need to pass new config, pointer is passively updated)
                    self._init_cameras()
                    self._set_crontabs()

    return SnapCam
