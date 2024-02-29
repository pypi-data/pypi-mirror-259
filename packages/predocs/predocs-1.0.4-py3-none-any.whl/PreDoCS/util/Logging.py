"""
Logging for PreDoCS.

.. codeauthor:: Daniel Hardt <daniel@daniel-hardt.de>
.. codeauthor:: Edgar Werthen <Edgar.Werthen@dlr.de>
"""
#   Copyright (c): 2024 Deutsches Zentrum fuer Luft- und Raumfahrt (DLR, German Aerospace Center) <www.dlr.de>. All rights reserved.

import logging
from contextlib import ContextDecorator


logging.captureWarnings(True)


def get_module_logger(mod_name):
    logger = logging.getLogger(mod_name)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    fh = logging.FileHandler('predocs.log')
    fh.setFormatter(formatter)
    fh.setLevel(logging.DEBUG)
    logger.addHandler(fh)

    return logger


log = get_module_logger(__name__)

try:
    from lightworks.utils.globals import DuplicateFilter

except ImportError:
    log.info('Modul lightworks.utils.globals not found. Use PreDoCS DuplicateFilter.')


    class DuplicateFilter(ContextDecorator):
        """
        Filters away duplicate log messages.
        Modified version of: https://stackoverflow.com/a/31953563/965332
        """

        def __init__(self, logger):
            self.msgs = set()
            self.logger = logger

        def filter(self, record):
            msg = str(record.msg)
            is_duplicate = msg in self.msgs
            if not is_duplicate:
                self.msgs.add(msg)
            return not is_duplicate

        def __enter__(self):
            self.logger.addFilter(self)

        def __exit__(self, exc_type, exc_val, exc_tb):
            if self in self.logger.filters:
                self.logger.removeFilter(self)
