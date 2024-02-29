"""Gets the idle time of the system"""
import logging
import importlib
from .scripts.helpers import import_install_package

logger = logging.getLogger("lnxlink")


class Addon:
    """Addon module"""

    def __init__(self, lnxlink):
        """Setup addon"""
        self.name = "Idle"
        self._requirements()
        if self.lib["dbus_idle"] is None:
            raise SystemError("Python package 'dbus_idle' can't be installed")

    def _requirements(self):
        self.lib = {
            "dbus_idle": import_install_package(
                "dbus-idle", ">=2023.12.0", "dbus_idle"
            ),
        }

    def get_info(self):
        """Gather information from the system"""
        try:
            idle_ms = self.lib["dbus_idle"].IdleMonitor().get_dbus_idle()
            idle_sec = round(idle_ms / 1000, 0)
            return idle_sec
        except NotImplementedError:
            logger.error("Unsupported version of dbus-idle found. Try to update...")
            import_install_package(
                "dbus-idle", ">=2023.12.0", "dbus_idle", forceupgrade=True
            )
            importlib.reload(self.lib["dbus_idle"])
            return 0
        except Exception as err:
            logger.error(err)
            return 0

    def exposed_controls(self):
        """Exposes to home assistant"""
        return {
            "Idle": {
                "type": "sensor",
                "icon": "mdi:timer-sand",
                "unit": "s",
                "state_class": "total_increasing",
                "device_class": "duration",
            },
        }
