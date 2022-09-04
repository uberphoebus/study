import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_option')
time.sleep(3)

browser.switch_to.frame('iframeResult') # iframe 전환

# 드롭다운 내부의 4번째 옵션 선택
elem = browser.find_element(by='xpath', value='//*[@id="cars"]/option[4]')
elem.click()

time.sleep(1)

# 텍스트 완전 일치
elem = browser.find_element(by='xpath', value='//*[@id="cars"]/option[text()="Opel"]')
elem.click()

time.sleep(1)

# 텍스트 부분 일치
elem = browser.find_element(by='xpath', value='//*[@id="cars"]/option[contains(text(), "Vol")]')
elem.click()