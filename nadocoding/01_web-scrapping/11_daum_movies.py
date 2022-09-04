import requests
import re
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}

for year in range(2015, 2020):
    print(f'페이지 : {year}')
    url = f'https://search.daum.net/search?w=tot&q={year}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR'
    
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')
    
    images = soup.find_all('img', attrs={'class':'thumb_img'})
    for idx, image in enumerate(images):
        image_url = image['src']
        if image_url.startswith('//'):
            image_url = f'https:{image_url}'
        
        image_res = requests.get(image_url)
        image_res.raise_for_status()
        
        with open(r'C:\workspace\mlProject\basic_webscrapping' + f'\movie_{year}_{idx + 1}.jpg', 'wb') as f:
            f.write(image_res.content)
        
        if idx >= 4:
            break