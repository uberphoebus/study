from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_experimental_option(
    'prefs', 
    {'download.default_directory':r'C:\workspace\avatarProject\basic_rpa\3_web'}
)

browser = webdriver.Chrome(options=chrome_options)
url = 'https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download'
browser.get(url)

time.sleep(3)
browser.switch_to.frame('iframeResult')

elem = browser.find_element(by='xpath', value='/html/body/p[2]/a')
elem.click()


time.sleep(3)
browser.quit()