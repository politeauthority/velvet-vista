"""
    Velvet Vista
    Modules
    Remote Version

    Get the remote version number of a given service.
"""

import logging

# from glom import glom

from velvet_vista.utils import web_tools
from velvet_vista.services import SERVICES


class RemoteVersion:

    def __init__(self):
        self.data = {
            "current": {},
            "latest": {}
        }

    def run(self, name: str, service: dict) -> dict:
        """Primary entrypoint for RemoteVersion.
        """
        self.service_name = name
        self.service_user = service
        self.service_base = SERVICES[self.service_name]
        logging.info(f"Getting upstream version of {self.service_name}")
        self.response = self.get_version()

    def get_version(self):
        data = self.github_release_fetch()
        version = self.github_release_parse(data)
        return version

    def github_release_fetch(self):
        owner = self.service_base["remotes"]["github_release"]["owner"]
        repo = self.service_base["remotes"]["github_release"]["repo"]
        url = f"https://api.github.com/repos/{owner}/{repo}/releases"
        response = web_tools.make_request(url)
        response_json = response.json()
        return response_json

    def github_release_parse(self, data):
        versions = []
        for release in data:
            versions.append(release["name"])
                
# End File: politeauthority/velvet-vista/src/velvet-vista/modules/remote_version.py
