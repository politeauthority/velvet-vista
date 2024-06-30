"""
    Velvet Vista
    Version Check
"""


class VersionCheck:

    def run(self):
        print("hello")

    def get_version_github(self):
        """
        """
        print("getting version")

    def get_sonarr(self):
        owner = "Sonarr"
        repo = "Sonarr"
        url = f"https://github.com/{owner}/{repo}/releases"
        response = request.get(url)
        import ipdb; ipdb.set_trace()



if __name__ == "__main__":
    print("hello")
    VersionCheck().run()


# End File: politeauthority/velvet-vista/src/velvet-vista/version-check.py