"""
Manage the logging system of the application
"""

import logging


def setup_logging(args):
    """Setup the logging system"""
    log_levels = ["WARNING", "INFO", "DEBUG"]
    logging.basicConfig(level=log_levels[args.verbose])


def warn(message):
    """WARNING"""
    logging.warning(" %s", message)


def info(message):
    """INFO"""
    logging.info(" %s", message)


def debug(message):
    """DEBUG"""
    logging.debug(" %s", message)


def critical(message):
    """CRITICAL"""
    logging.critical(" %s", message)
