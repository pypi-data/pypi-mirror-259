import time
import logging

from onvif import ONVIFCamera

logger = logging.getLogger(__name__)

def reboot_camera(cam: ONVIFCamera):
    """Administrator-level ONVIF user needed"""

    service = cam.create_devicemgmt_service()
    reboot_request = service.create_type("SystemReboot")
    #reboot_request.ProfileToken = service.GetProfiles()[0].token
    msg = service.SystemReboot(reboot_request)
    logger.info("Scheduling a camera reboot: %s", msg)

#class CamManagement:
#    """Device management endpoint for onvif camera."""
#
#    def __init__(self, cam: ONVIFCamera):
#        self._devicemgmt_service = cam.create_devicemgmt_service()
#
#    def reboot(self):
#        """Reboot the camera."""
#        reboot_request = self._devicemgmt_service.create_type("SystemReboot")
#        print(self._devicemgmt_service.SystemReboot(reboot_request))

class PTZ:
    """A wrapper for useful PTZ (Pan&Tilt&Zoom) actions. Operator ONVIF user priviliges."""

    def __init__(self, cam: ONVIFCamera):
        """
        cam: ONVIFCamera object
        """
        # create ptz (pan tilt zoom) service object
        self._ptz_service = cam.create_ptz_service()

        # get media service token
        media = cam.create_media_service()
        self._media_token = media.GetProfiles()[0].token
        self._ptz_token = media.GetProfiles()[0].PTZConfiguration.token

        # configuration request to get bounds on AbsoluteMove and RelativeMove action space (range of movement) + speeds
        self.conf = self.get_ptz_configuration()

    def absolute_move(self, x, y, zoom):
        """
        Moves camera to absolute position specified by x, y coordinates and zooms.
        x: rotation with respect to axis going perpendicularly through ceiling
        y: up/down rotation, rotation with respect to axis going parallel with ceiling
        Common ranges for x, y and zoom are [-1,1], [-1,1] and [0,1] respectively but it depends on particular camera.
        """
        # check x coordinate
        assert (
            self.conf.Spaces.AbsolutePanTiltPositionSpace[0].XRange.Min
            <= x
            <= self.conf.Spaces.AbsolutePanTiltPositionSpace[0].XRange.Max
        ), "x coordinate is not in bounds specified by camera"

        # check y coordinate
        assert (
            self.conf.Spaces.AbsolutePanTiltPositionSpace[0].YRange.Min
            <= y
            <= self.conf.Spaces.AbsolutePanTiltPositionSpace[0].YRange.Max
        ), "y coordinate is not in bounds specified by camera"

        # check zoom coordinate
        assert (
            self.conf.Spaces.AbsoluteZoomPositionSpace[0].XRange.Min
            <= zoom
            <= self.conf.Spaces.AbsoluteZoomPositionSpace[0].XRange.Max
        ), "zoom is not in bounds specified by camera"

        # create request to AbsoluteMove
        # Arguments: ProfileToken [ReferenceToken], Position [PTZVector], Speed - optional [PTZSpeed]
        absmove_request = self._ptz_service.create_type("AbsoluteMove")
        absmove_request.ProfileToken = self._media_token

        # == set actual move instructions ==
        absmove_request.Position = {
            "PanTilt": {
                "x": x,
                "y": y,
                "space": (
                    "http://www.onvif.org/ver10/tptz/PanTiltSpaces/PositionGenericSpace"
                ),
            },
            "Zoom": {
                "x": zoom,
                "space": (
                    "http://www.onvif.org/ver10/tptz/ZoomSpaces/PositionGenericSpace"
                ),
            },
        }

        # - set maximum speeds so that the action takes least amount of time
        # there is no PanTiltSpeedSpace[0].YRange, x and y share XRange speed space
        absmove_request.Speed = {
            "PanTilt": {
                "x": self.conf.Spaces.PanTiltSpeedSpace[0].XRange.Max,
                "y": self.conf.Spaces.PanTiltSpeedSpace[0].XRange.Max,
                "space": (
                    "http://www.onvif.org/ver10/tptz/PanTiltSpaces/GenericSpeedSpace"
                ),
            },
            "Zoom": {
                "x": self.conf.Spaces.ZoomSpeedSpace[0].XRange.Max,
                "space": (
                    "http://www.onvif.org/ver10/tptz/ZoomSpaces/ZoomGenericSpeedSpace"
                ),
            },
        }

        # send request
        self._ptz_service.AbsoluteMove(absmove_request)

    def relative_move(self, x, y, zoom):
        """
        Moves camera along vector specified by x, y coordinates and zooms. This is a RELATIVE translation as opposed to
            setting ABSOLUTE coordinates of self.absolute_move.
        The camera stops when it can continue no further.
        x: rotation with respect to axis going perpendicularly through ceiling
        y: up/down rotation, rotation with respect to axis going parallel with ceiling
        Common ranges for x, y and zoom are [-1,1], [-1,1] and [0,1] respectively but it depends on particular camera.
        """
        # check x coordinate
        assert (
            self.conf.Spaces.RelativePanTiltTranslationSpace[0].XRange.Min
            <= x
            <= self.conf.Spaces.RelativePanTiltTranslationSpace[0].XRange.Max
        ), "x coordinate is not in bounds specified by camera"

        # check y coordinate
        assert (
            self.conf.Spaces.RelativePanTiltTranslationSpace[0].YRange.Min
            <= y
            <= self.conf.Spaces.RelativePanTiltTranslationSpace[0].YRange.Max
        ), "y coordinate is not in bounds specified by camera"

        # check zoom coordinate
        assert (
            self.conf.Spaces.RelativeZoomTranslationSpace[0].XRange.Min
            <= zoom
            <= self.conf.Spaces.RelativeZoomTranslationSpace[0].XRange.Max
        ), "zoom is not in bounds specified by camera"

        # create request to RelativeMove
        # Arguments: ProfileToken [ReferenceToken], Translation [PTZVector], Speed - optional [PTZSpeed]
        relmove_request = self._ptz_service.create_type("RelativeMove")
        relmove_request.ProfileToken = self._media_token

        # == set actual move instructions ==
        # - copy structure of correct response from current position
        relmove_request.Translation = {
            "PanTilt": {
                "x": x,
                "y": y,
                "space": "http://www.onvif.org/ver10/tptz/PanTiltSpaces/TranslationGenericSpace",
            },
            "Zoom": {
                "x": zoom,
                "space": (
                    "http://www.onvif.org/ver10/tptz/ZoomSpaces/TranslationGenericSpace"
                ),
            },
        }

        # - set maximum speeds so that the action takes least amount of time
        relmove_request.Speed = {
            "PanTilt": {
                "x": self.conf.Spaces.PanTiltSpeedSpace[0].XRange.Max,
                "y": self.conf.Spaces.PanTiltSpeedSpace[0].XRange.Max,
                "space": (
                    "http://www.onvif.org/ver10/tptz/PanTiltSpaces/GenericSpeedSpace"
                ),
            },
            "Zoom": {
                "x": self.conf.Spaces.ZoomSpeedSpace[0].XRange.Max,
                "space": (
                    "http://www.onvif.org/ver10/tptz/ZoomSpaces/ZoomGenericSpeedSpace"
                ),
            },
        }

        # send request
        self._ptz_service.RelativeMove(relmove_request)

    def wait_for_move(self):
        """
        Block until movement of the camera is finished.
        """
        time.sleep(0.1)  # update move status
        status = self.get_move_status()
        while status.PanTilt == "MOVING" or status.Zoom == "MOVING":
            status = self.get_move_status()
            time.sleep(0.2)
        return True

    def get_status(self):
        return self._ptz_service.GetStatus({"ProfileToken": self._media_token})
        # >>> ptz.GetStatus({'ProfileToken': media_profile.token}).Position
        # {
        #     'PanTilt': {
        #         'x': -0.027778,
        #         'y': -1.0,
        #         'space': 'http://www.onvif.org/ver10/tptz/PanTiltSpaces/PositionGenericSpace'
        #     },
        #     'Zoom': {
        #         'x': 0.0,
        #         'space': 'http://www.onvif.org/ver10/tptz/ZoomSpaces/PositionGenericSpace'
        #     }
        # }

    def get_move_status(self):
        return self.get_status().MoveStatus

    def get_ptz_configuration(self):
        """
        Get PTZ configuration (to set movement bounds).
        """
        # configuration request to get bounds on action space (range of movement)
        request = self._ptz_service.create_type("GetConfigurationOptions")
        request.ConfigurationToken = self._ptz_token
        ptz_configuration_options = self._ptz_service.GetConfigurationOptions(request)
        return ptz_configuration_options

        # >>> ptz_configuration_options.Spaces
        # {
        #     'AbsolutePanTiltPositionSpace': [
        #         {
        #             'URI': 'http://www.onvif.org/ver10/tptz/PanTiltSpaces/PositionGenericSpace',
        #             'XRange': {
        #                 'Min': -1.0,
        #                 'Max': 1.0
        #             },
        #             'YRange': {
        #                 'Min': -1.0,
        #                 'Max': 1.0
        #             }
        #         }
        #     ],
        #     'AbsoluteZoomPositionSpace': [
        #         {
        #             'URI': 'http://www.onvif.org/ver10/tptz/ZoomSpaces/PositionGenericSpace',
        #             'XRange': {
        #                 'Min': 0.0,
        #                 'Max': 1.0
        #             }
        #         }
        #     ],
        #     'PanTiltSpeedSpace': [
        #         {
        #             'URI': 'http://www.onvif.org/ver10/tptz/PanTiltSpaces/GenericSpeedSpace',
        #             'XRange': {
        #                 'Min': 0.0,
        #                 'Max': 1.0
        #             }
        #         }
        #     ], ... }
