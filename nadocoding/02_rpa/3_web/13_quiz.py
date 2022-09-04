# 1. w3schools 접속
# 2. LEARN HTML 클릭
# 3. 상단 메뉴 중 HOW TO 클릭
# 4. 좌측 메뉴 중 Contact From 메뉴 클릭
# 5. 입력 나도 / 코딩 / Canada / 퀴즈 완료하였습니다.
# 6. 5초 대기 후 Submit 클릭
# 7. 5초 대기 후 브라우저 종료

import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.w3schools.com/')
browser.maximize_window()
time.sleep(3)

browser.find_element('xpath', '//*[@id="main"]/div[2]/div/div[1]/a[1]').click()
time.sleep(1)

browser.find_element('xpath', '//*[@id="topnav"]/div/div/a[10]').click()
time.sleep(1)

# browser.find_element('xpath', '//*[@id="leftmenuinnerinner"]/a[117]').click()
# browser.find_element('link_text', 'Contact Form')
browser.find_element('xpath', '//*[@id="leftmenuinnerinner"]/a[text()="Contact Form"]').click()
time.sleep(1)

texts = ['나도', '코딩', 'Canada', '퀴즈 완료']

browser.find_element('xpath', '//*[@id="fname"]').send_keys(texts[0])
browser.find_element('xpath', '//*[@id="lname"]').send_keys(texts[1])
browser.find_element(by='xpath', value=f'//*[@id="country"]/option[text()="{texts[2]}"]').click()
browser.find_element('xpath', '//*[@id="main"]/div[3]/textarea').send_keys(texts[3])

time.sleep(3)
browser.find_element('xpath', '//*[@id="main"]/div[3]/a').click()

time.sleep(2)
browser.quit()