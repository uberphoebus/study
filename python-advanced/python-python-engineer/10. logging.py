import logging
import os

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%Y/%m/%d %H:%M:%S')

logging.debug('debug')
logging.info('info')

# default print logging level
logging.warning('warning')
logging.error('error')
logging.critical('critical')

import helper


logger = logging.getLogger(__name__)

# create handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler(os.path.join(os.getcwd(), 'study', 'python-advanced', 'python-python-engineer', 'file.log'))

# level and format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('this is a warning')
logger.error('this is a error')

print('-'*30)

import traceback

try:
    a = [1, 2, 3]
    val = a[4]
except IndexError as e:
    logging.error(e, exc_info=True)
except:
    logging.error('the error is %s',
                  traceback.format_exc())