"""
    Velvet Vista
    Version Check

    Primary entrpoint for log checking.

"""

import logging

from utils import glow
from utils import logger
# from utils import web_tools
from velvet_vista.modules.read_version import ReadVersion


class VersionCheck:

    def __init__(self):
        logger.setup_logger()
        logging.info("Logger setup")

    def run(self):
        logging.info("Starting checks")
        service_name = "sonarr"
        service = glow.CONFIG["services"][service_name]
        self.check_service(service_name, service)
        # self.get_local_version()
        # self.get_local_version()
        # self.get_version_github()

    def check_service(self, service: dict) -> bool:
        read_version = ReadVersion().run(service)
        print(read_version)

    def get_version_github(self):
        """
        """
        print("getting version")
        self.get_sonarr()

    def get_sonarr(self):
        owner = "Sonarr"
        repo = "Sonarr"
        self.get_github_releases(owner, repo)

    # def get_github_releases(self, owner: str, repo: str):
    #     url = f"https://api.github.com/repos/{owner}/{repo}/releases"
    #     response = requests.get(url)


if __name__ == "__main__":
    VersionCheck().run()


# End File: politeauthority/velvet-vista/src/velvet-vista/version-check.py
