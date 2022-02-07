import requests
import os

os.chdir(r'C:\workspace\mlProject\basic_webscrapping')

res = requests.get('http://google.com')

if res.status_code == requests.codes.ok:
    print(f'정상 {res.status_code}')
else:
    print(f'오류 {res.status_code}')

res.raise_for_status() # 오류 발생시 종료
print('진행')

with open('mygoogle.html', 'w', encoding='utf8') as f:
    f.write(res.text)