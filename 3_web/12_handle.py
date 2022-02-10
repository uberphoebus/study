import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.maximize_window()

browser.get('https://www.w3schools.com/tags/att_input_type_radio.asp')
time.sleep(3)

curr_handle = browser.current_window_handle
print(curr_handle)

browser.find_element(by='xpath', value='//*[@id="main"]/div[2]/a').click()

handles = browser.window_handles # 모든 핸들 정보
for handle in handles:
    print(handle)
    browser.switch_to.window(handle) # 핸들 이동
    print(browser.title) # 제목 출력

# 브라우저 종료
browser.close()

# 이전 핸들로 돌아오기
browser.switch_to.window(curr_handle)
print(browser.title)

time.sleep(3)
browser.quit()