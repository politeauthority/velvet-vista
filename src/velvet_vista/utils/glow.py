"""
    Glow
    Global variables helper.

"""
import logging
import os

import yaml

from velvet_vista.services import SERVICES


CONFIG_FILE = "/configs/config.yaml"


def load_config() -> dict:
    """Load config combinding the file and defaults to make a consolidated configuration. """
    config_file = read_config_file()
    configs = get_defaults()
    configs.update(config_file)
    validate_config(configs)
    return configs


def read_config_file() -> dict:
    """Read the yaml config and send it back."""
    if not os.path.exists(CONFIG_FILE):
        logging.warning(f"No config file found at {CONFIG_FILE} using all defaults.")
        return {}
    with open(CONFIG_FILE, "r") as phile:
        yaml_config = yaml.safe_load(phile)
    user_config = yaml_config["velvet-vista"]
    return user_config


def get_defaults() -> dict:
    """Setup and supply the default configuraton makeup."""
    defaults = {
        "general": {
            "log_level": "DEBUG",
        },
        "notfications": {},
        "services": {},
    }
    return defaults


def validate_config(configs) -> bool:
    return True
    # available_services = SERVICES.keys()


global CONFIG
CONFIG = load_config()

# End File: politeauthority/velvet-vista/src/velvet-vista/utils/glow.py
