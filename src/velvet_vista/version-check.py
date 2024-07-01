"""
    Velvet Vista
    Version Check

    Primary entrpoint for log checking.

"""

import logging

from utils import glow
from utils import logger
from velvet_vista.modules.local_version import LocalVersion
from velvet_vista.modules.remote_version import RemoteVersion
from velvet_vista.__version__ import version


class VersionCheck:

    def __init__(self):
        logger.setup_logger()
        logging.info("Logger setup")

    def run(self):
        logging.info(f"Running Version Check: v{version}")
        service_name = "sonarr"
        service = glow.CONFIG["services"][service_name]
        self.check_service(service_name, service)
        # self.get_local_version()
        # self.get_local_version()
        # self.get_version_github()

    def check_service(self, service_name: str, service_user: dict) -> bool:
        local_ver = LocalVersion().run(service_name, service_user)
        remote_ver = RemoteVersion().run(service_name, service_user)
        print(local_ver)
        import ipdb; ipdb.set_trace()

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
