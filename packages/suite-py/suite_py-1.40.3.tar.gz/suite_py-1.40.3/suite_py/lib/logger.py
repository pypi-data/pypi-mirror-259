# -*- encoding: utf-8 -*-
import logging

import logzero
from logzero import logger as _logger

DEFAULT_FORMAT = "%(color)s[%(levelname)1.4s]%(end_color)s %(message)s"
# Set a custom formatter
formatter = logzero.LogFormatter(fmt=DEFAULT_FORMAT)
logzero.setup_default_logger(formatter=formatter)
_logger.setLevel(logging.INFO)


def setLevel(level):
    _logger.setLevel(level)


def debug(message, *args, **kwargs):
    _logger.debug(message, *args, **kwargs)


def info(message, *args, **kwargs):
    _logger.info(message, *args, **kwargs)


def warning(message, *args, **kwargs):
    _logger.warning(message, *args, **kwargs)


def error(message, *args, **kwargs):
    _logger.error(message, *args, **kwargs)
