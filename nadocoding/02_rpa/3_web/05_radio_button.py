from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')
time.sleep(3)

browser.switch_to.frame('iframeResult') # iframe 전환
elem = browser.find_element(by='xpath', value='//*[@id="html"]')

if elem.is_selected() == False: # 선택 안되어 있다면
    elem.click()
else:
    pass

browser.quit()