"""
    Velvet Vista
    Modules
    Local Version

"""

import logging

# from glom import glom

from velvet_vista.utils import web_tools
from velvet_vista.services import SERVICES


class LocalVersion:

    def run(self, name: str, service: dict) -> dict:
        """Primary entrypoint for ReadLocalVersion.
        """
        self.service_name = name
        self.service_user = service
        self.service_base = SERVICES[self.service_name]
        logging.info(f"Reading version of {self.service_name}")
        self.response = self.get_version()
        if not self.response:
            logging.error(f"Failed to get version info from {name}")
            return False
        else:
            logging.info(f"{self.service_name} response {self.response.status_code}")
        parsed = self.parse_response()
        if not parsed:
            logging.error("Failed - {self.service_name}")
            return False
        version = {
            "raw": parsed
        }
        return version

    def get_version(self):
        url = web_tools.url_concat([self.service_user["api_url"], self.service_base["url"]])
        api_key = self.service_user["api_key"]
        headers = {
            "X-Api-Key": api_key
        }
        response = web_tools.make_request(url, headers=headers)
        if not response:
            logging.error(f"Error fetching version from: {self.service_name}")
            return False
        return response

    def parse_response(self) -> str:
        """
        @todo: Make this understand where to parse.
        """
        rj = self.response.json()
        data = rj[0]
        if "version" not in data:
            error_msg = "Parse - could not find version path in response - "
            error_msg += f"{self.response.status_code}"
            logging.error(error_msg)
            return False
        return data["version"]

# End File: politeauthority/velvet-vista/src/velvet-vista/modules/local_version.py
