"""
    Velvet Vista
    Services

"""
SERVICES = {
    "sonarr": {
        "local": {

        },
        "remotes": {
            "github_release": {
                "owner": "Sonarr",
                "repo": "sonarr",
            }
        },
        "name": "sonarr",
        "url": "api/v3/update",
        "json_path": "[0].version",
        "reponse_type": "json",
    }
}

# End File: politeauthority/velvet-vista/src/velvet-vista/services.py
