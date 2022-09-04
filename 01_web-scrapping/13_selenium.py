from selenium import webdriver

browser = webdriver.Chrome(r'basic_webscrapping\chromedriver.exe')

# 네이버 이동
browser.get('http://naver.com')

# 로그인 버튼 클릭
elem = browser.find_element('class', 'link_login')
elem.click()