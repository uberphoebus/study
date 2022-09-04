import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome()

url = 'https://www.w3schools.com/html/'
browser.get(url)
browser.maximize_window()
time.sleep(5)

elem = browser.find_element(by='xpath', value='//*[@id="leftmenuinnerinner"]/a[62]')

# ActionChain
# actions = ActionChains(browser)
# actions.move_to_element(elem).perform()

# 좌표정보 이동
xy = elem.location_once_scrolled_into_view
elem.click()

time.sleep(3)