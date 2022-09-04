from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(r'basic_webscrapping\chromedriver.exe')
browser.maximize_window()

# 네이버 이동
url = 'https://flight.naver.com/'
browser.get(url)

try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]')))
    elem.click()
finally:
    browser.quit()