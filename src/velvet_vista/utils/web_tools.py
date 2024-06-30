"""
    Velvet Vista
    Utils
    Web Tools
"""
import logging

import requests


def make_request(url: str, headers: dict) -> dict:
    """Make a generic request, catching the errors we can anticipate.
    """
    logging.info(f"Fetching url: {url}")
    response = requests.get(url, headers=headers)
    if response.status_code > 299:
        logging.error(f"Error fetching url: {url}")
        return False

    return response

# End File: politeauthority/velvet-vista/src/velvet-vista/utils/web_tools.py
