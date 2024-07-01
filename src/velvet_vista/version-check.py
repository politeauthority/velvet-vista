"""
    Velvet Vista
    Version Check

    Primary entrpoint for log checking.

"""

import logging

from velvet_vista.utils import glow
from velvet_vista.utils import logger
from velvet_vista.modules.local_version import LocalVersion
from velvet_vista.modules.remote_version import RemoteVersion
from velvet_vista.__version__ import version


class VersionCheck:

    def __init__(self):
        logger.setup_logger()
        logging.debug("Logger setup")
        self.data = {
            "report": {
                "services": {}
            }
        }

    def run(self):
        """Primary entrypoint for VersionCheck. We'll 
        """
        logging.info(f"Running Version Check: v{version}")
        self.check_services()
        self.report_services()

    def check_services(self):
        """Iterate through all the user defined services"""
        logging.info("Checking %s configured services" % len(glow.CONFIG["services"]))
        for service_name, service in glow.CONFIG["services"].items():
            if not service["enabled"]:
                logging.debug("Service {service_name} not enabled by user config")
                continue
            self.check_service(service_name, service)

    def report_services(self):
        logging.info("REPORT SECTION")
        print(self.data)

    def check_service(self, service_name: str, service_user: dict) -> bool:
        local_ver = LocalVersion().run(service_name, service_user)
        remote_ver = RemoteVersion().run(service_name, service_user)
        self.compare_ver(service_name, local_ver, remote_ver)
        return True

    def compare_ver(self, service_name: str, local_ver: dict, remote_ver: dict) -> bool:
        data = {}
        data["compliance"] = None
        logging.debug(f"{service_name} - Comparing")
        local_v_num = local_ver["raw"]
        remote_v_num = remote_ver["latest"]["version"]

        if local_v_num != remote_v_num:
            logging.warning(
                f"{service_name} - Local Version {local_v_num} - Remote Latest: {remote_v_num}")
            data["compliance"] = False
        else:
            data["compliance"] = False
        self.data["report"]["services"][service_name] = data
        return True


if __name__ == "__main__":
    VersionCheck().run()


# End File: politeauthority/velvet-vista/src/velvet-vista/version-check.py
