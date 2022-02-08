import requests
from bs4 import BeautifulSoup
import time

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    'Accept-Language':'ko-KR,ko'
}
url = 'https://play.google.com/store/movies'
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

movies = soup.find_all('div', attrs={'class':'VfPpkd-EScbFb-JIbuQc UVEnyf'})

# with open('movie.html', 'w', encoding='utf8') as f:
#     f.write(soup.prettify())

for movie in movies:
    title = movie.find('div', attrs={'class':'Epkrse'}).get_text()
    print(title)