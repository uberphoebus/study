import time
from cv2 import borderInterpolate
from selenium import webdriver

browser = webdriver.Chrome()
browser.maximize_window()

url = 'https://shopping.naver.com/home/p/index.naver'
browser.get(url)
time.sleep(3)

# 무선마우스 입력
browser.find_element(by='xpath', value='//*[@id="autocompleteWrapper"]/input[1]').send_keys('무선마우스')
browser.find_element(by='xpath', value='//*[@id="autocompleteWrapper"]/a[2]').click()

time.sleep(3)

# 1080 위치로 스크롤
browser.execute_script('window.scrollTo(0, 1090)')

time.sleep(1)

# 화면 가장 아래로 스크롤
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')


# 스크롤 반복수행
interval = 2
prev_height = browser.execute_script('return document.body.scrollHeight')
while True:
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    
    time.sleep(interval)
    curr_height = browser.execute_script('return document.body.scrollHeight')
    if curr_height == prev_height:
        break
    
    prev_height = curr_height
