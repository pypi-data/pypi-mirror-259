import logging
from io import BytesIO

import requests

import onvif
from onvif import ONVIFCamera

from .onvif_soap import PTZ

# imported
from .onvif_soap import reboot_camera

logger = logging.getLogger(__name__)


class DownloadException(Exception):
    pass

def create_camera(ip, port, user, password, wsdl):
    """ Create a camera object. """
    return ONVIFCamera(ip, port, user, password, wsdl)

class SnapSequence:
    """
    A class for managing ONVIF camera to take snapshot-like panorama.
    Moves camera along a given path of coordinates and takes pictures.
    """

    def __init__(self, cam: ONVIFCamera, user, password, positions):
        """
        cam:        ONVIFCamera instance
        user:       ONVIF user with sufficient permissions
        password:   ONVIF user's password
        wsdl:       location to wsdl files (protocol)
        positions:  list of locations to visit [{'x': ..., 'y': ..., 'zoom': ...}, ...]
        """
        self._cam = cam
        self._user = user
        self._password = password
        self._ptz = PTZ(self._cam)

        # get snapshot URI for downloading snapshots
        media = self._cam.create_media_service()
        media_profile = media.GetProfiles()[0]
        snapshot_uri_resp = media.GetSnapshotUri({"ProfileToken": media_profile.token})

        self._snapshot_uri = snapshot_uri_resp.Uri
        self._positions = positions

    @staticmethod
    def from_credentials(ip, port, user, password, wsdl, positions):
        """
        ip:         ONVIFCamera IP address
        port:       ONVIFCamera port number
        user:       ONVIF user with sufficient permissions
        password:   ONVIF user's password
        wsdl:       location to wsdl files (protocol)
        positions:  list of locations to visit [{'x': ..., 'y': ..., 'zoom': ...}, ...]
        """
        return SnapSequence(
            create_camera(ip, port, user, password, wsdl),
            user, password, positions)

    def _download_snapshot(self):
        resp = requests.get(
            self._snapshot_uri,
            auth=requests.auth.HTTPDigestAuth(self._user, self._password),
        )

        if 200 <= resp.status_code < 300:
            return BytesIO(resp.content)
        else:
            raise DownloadException("Cannot download image from camera.")

    def loop(self, callback):
        """
        Visit every location provided in self.positions.
        callback: a void function (image_binary, position) -> None to be called after taking a single snapshot
        """
        i = -1
        logger.debug("Starting snapshot loop.")

        for position in self._positions:
            i += 1
            x = position["x"]
            y = position["y"]
            zoom = position["zoom"]
            name = position["name"] if "name" in position else "unnamed"

            logger.info(
                f'Moving camera to position "{name}" @ (x={x}, y={y}, zoom={zoom})...'
            )
            try:
                self._ptz.absolute_move(x, y, zoom)
                self._ptz.wait_for_move()
            except onvif.ONVIFError as e:
                logger.warning("Onvif error on camera move: %s", str(e))
                continue

            # output single snapshot
            snapshot_bin = self._download_snapshot()
            callback(snapshot_bin, position)

            logger.debug("Snapshot %i taken.", i)

        # reset to initial position
        # self.ptz.absolute_move(0, 0, 0)

        logger.debug("Loop finished.")
