

# web
from flask import Flask, make_response, jsonify, request, render_template
import requests
from bs4 import BeautifulSoup

# parsing
import json
import xmltodict
from pandas.io.json import json_normalize

# others
import pandas as pd
import numpy as np
import datetime
from pykrx import stock


# flask
app = Flask(__name__)


def crawl(url):
    
    '''YTN 경제기사 크롤링'''
    
    # url에서 html 추출
    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
    else:
        print('error', response.status_code)
    
    # 기사별 태그 리스트
    article_list = soup.select("#zone1 > div > div.newslist_wrap > div:nth-child(1) > ul > li")
    
    # 기사 담는 리스트
    news_list = []
    for i, li_tag in enumerate(list):
        
        dict = {}
        title = li_tag.select_one('a > div > span').text
        rdate = li_tag.select_one('a > div > div > span.date').text
        url   = li_tag.select_one('a').get('href')
        
        dict['key_title'] = title
        dict['key_rdate'] = rdate
        dict['key_url']   = url
        
        news_list.append(dict)
    
    news_list = news_list[:5]
    
    return news_list


def etf_list_json():
    
    '''NAVER금융에서 ETF 크롤링'''
    
    url = 'https://finance.naver.com/api/sise/etfItemList.nhn'
    
    # url의 html을 text로 받아, json 형태로 가져오기
    json_data = json.loads(requests.get(url).text)




# flask 연결
@app.route('/')
def index():
    
    return

# py 실행 시 동작
if __name__ == '__main__':
    
    app.run(
        host='127.0.0.1', # 주소
        port=8088,        # 포트 : 임의로 할당 가능
        debug=True        # py 변경시 재실행
    )