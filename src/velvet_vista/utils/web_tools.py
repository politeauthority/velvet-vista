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


def url_concat(url_parts: list) -> str:
    """Add url parts together with the propper slashes to segment the peices.
    @todo: Finish this, support more than 2 parts, more error checking.
    """
    full_url = ""
    full_url = url_parts[0]
    if url_parts[0][-1] != "/":
        full_url += "/"
    full_url = full_url + url_parts[1]
    return full_url
    # for url_part in url_parts:
    #     full_url += url_part
    #     count += 1

# End File: politeauthority/velvet-vista/src/velvet-vista/utils/web_tools.py
