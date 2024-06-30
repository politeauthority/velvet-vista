"""
    Velvet Vista
    Modules
    Read Version
"""

import logging

from velvet_vista.utils import web_tools

SERVICES = {
    "sonarr": {
        "name": "sonarr",
        "url": "api/v3/update",
        "json_path": "[0].version",
        "reponse_type": "json"
    }
}


class ReadVersion:

    def run(self, name: str, service: dict):
        self.service_name = name
        self.service_user = service
        self.service_base = SERVICES[self.service_name]
        logging.info(f"Reading version of {self.service_name}")
        self.get_version()

    def get_version(self):
        url = self.service_user["api_url"] + self.service_base["url"]
        api_key = self.service_user["api_key"]
        headers = {
            "X-Api-Key": api_key
        }
        response = web_tools.make_request(url, headers=headers)
        if not response:
            logging.error(f"Error fetching version from: {self.service_name}")
            return False
        response_json = response.json()
        print(response_json)


# End File: politeauthority/velvet-vista/src/velvet-vista/modules/read_version.py
