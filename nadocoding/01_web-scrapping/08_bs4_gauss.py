import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/list?titleId=675554'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')
cartoons = soup.find_all('td', attrs={'class':'title'})

for cartoon in cartoons:
    title = cartoon.a.get_text()
    link = 'https://comic.naver.com' + cartoon.a['href']
    print(title, link)

total_rates = 0
cs = soup.find_all('div', attrs={'class':'rating_type'})
for c in cs:
    rate = c.find('strong').get_text()
    print(rate)
    total_rates += float(rate)

print(total_rates / len(cs))