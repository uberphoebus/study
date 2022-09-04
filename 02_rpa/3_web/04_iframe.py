from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')
time.sleep(3)

browser.switch_to.frame('iframeResult') # iframe 전환
time.sleep(3)

elem = browser.find_element(by='xpath', value='//*[@id="html"]')
elem.click()
browser.switch_to_default_content()

time.sleep(3)
browser.quit()