import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    'Accept-Language':'ko-KR,ko'
}

url_w = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8'
url_n = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105'

res_w = requests.get(url_w, headers=headers)
res_n = requests.get(url_n, headers=headers)

res_w.raise_for_status()
res_n.raise_for_status()

soup_w = BeautifulSoup(res_w.text, 'lxml')
soup_n = BeautifulSoup(res_n.text, 'lxml')

weather = soup_w.find('div', attrs={'class':'status_wrap'}).get_text()
print(weather)

news = soup_n.find('ul', attrs={'class':'cluster_list'})
res = news.find_all('div', attrs={'class':'cluster_text'})
for i in res:
    print(i.text)

