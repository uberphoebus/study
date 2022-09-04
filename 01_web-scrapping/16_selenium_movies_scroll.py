import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver

browser = webdriver.Chrome('./basic_webscrapping/chromedriver.exe')
browser.maximize_window()

url = 'https://play.google.com/store/movies'
browser.get(url)

# 스크롤 내리기(모니터 높이)
# browser.execute_script('window.scrollTo(0, 1080)')

# 화면 가장 아래로
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

interval = 2

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script('return document.body.scrollHeight')

# 반복수행
while True:
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(interval)
    curr_height = browser.execute_script('return document.body.scrollHeight')
    
    if curr_height == prev_height:
        break
    
    prev_height = curr_height
print('스크롤 끝')


soup = BeautifulSoup(browser.page_source, 'lxml')

movies = soup.find_all('div', attrs={'class':'VfPpkd-EScbFb-JIbuQc UVEnyf'}) # attr는 리스트로도 가능
for movie in movies:
    title = movie.find('div', attrs={'class':'Epkrse'}).get_text()
    print(title)