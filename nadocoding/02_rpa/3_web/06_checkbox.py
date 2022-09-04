import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox')
time.sleep(3)

browser.switch_to.frame('iframeResult') # iframe 전환
elem = browser.find_element(by='xpath', value='//*[@id="vehicle1"]')

if elem.is_selected() == False: # 선택 안되어 있다면
    elem.click()
else:
    pass