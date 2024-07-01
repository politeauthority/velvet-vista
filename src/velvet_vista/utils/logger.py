"""
    Velvet Vista
    Utils
    Logger

    Custom logger for handling log events.

"""

import logging

LOG_LEVEL = logging.INFO


class CustomFormatter(logging.Formatter):
    def format(self, record):
        log_time = self.formatTime(record, "%Y-%m-%d %H:%M:%S")
        log_file = record.filename
        log_level = record.levelname
        the_format = f"{log_time} - {log_file} - {log_level}: {record.msg}"

        # the_format = f"{log_time} - {log_level}: {record.msg}"
        return the_format


def setup_logger():
    # Create a logging instance
    logger = logging.getLogger()
    logger.setLevel(LOG_LEVEL)

    # Create a file handler and set the level to INFO
    # file_handler = logging.FileHandler('app.log')
    # file_handler.setLevel(logging.INFO)

    # Create formatters for file and console handlers
    # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # file_handler.setFormatter(formatter)
    # console_handler.setFormatter(formatter)

    # Create a console handler and set the level to INFO
    console_handler = logging.StreamHandler()
    console_handler.setLevel(LOG_LEVEL)
    formatter = CustomFormatter()
    console_handler.setFormatter(formatter)

    # Add the handlers to the logger
    # logger.addHandler(file_handler)
    logger.addHandler(console_handler)

# End File: politeauthority/velvet-vista/src/velvet-vista/utils/logger.py
