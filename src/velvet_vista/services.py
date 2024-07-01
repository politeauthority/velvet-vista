"""
    Velvet Vista
    Services

"""
SERVICES = {
    "sonarr": {
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
    },
    "radarr": {
        "remotes": {
            "github_release": {
                "owner": "Radarr",
                "repo": "Radarr",
            }
        },
        "name": "radarr",
        "url": "api/v3/update",
        "json_path": "[0].version",
        "reponse_type": "json",
    }
}

# End File: politeauthority/velvet-vista/src/velvet-vista/services.py
