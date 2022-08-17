import logging

from sqlalchemy import false

logger = logging.getLogger(__name__)
# logger.propagate = False # not to show on base logger
logger.info('hello from helper')