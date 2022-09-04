import logging
from datetime import datetime

logging.basicConfig(
    level=logging.ERROR, # 레벨보다 높은 수준만
    format='%(asctime)s [%(levelname)s] %(message)s'
)

# debug < info < warning < error < critical
logging.debug('누가 짠거야~') # 개발 단계
logging.info('자동화 수행 준비')
logging.warning('경고문 문제')
logging.error('에러 발생')
logging.critical('복구 불가 에러')

# 터미널과 파일에 로그 남기기
logFormatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger()

# 로그 레벨 설정
logger.setLevel(logging.DEBUG)

# 스트림(터미널)
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logFormatter)
logger.addHandler(streamHandler)

# 파일
filename = datetime.now().strftime('mylogfile_%Y%m%d%H%M%S.log')
fileHandler = logging.FileHandler(filename, encoding='utf-8')
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)

logger.debug('로그 테스트')