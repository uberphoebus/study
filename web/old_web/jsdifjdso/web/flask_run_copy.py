
# --------------------------------------------------

# imports : web
from flask import Flask, make_response, jsonify, request, render_template
import requests

# imports : paser
from bs4 import BeautifulSoup
import json
import xmltodict
from pandas.io.json import json_normalize

# imports : others
import pandas as pd
import numpy as np
import datetime
from pykrx import stock

# --------------------------------------------------

# 서버 구성
app = Flask(__name__)

# --------------------------------------------------

# 라우터 내 사용할 함수들

def crawl(url):
    
    """YTN 경제기사 크롤링"""
    
    response = requests.get(url)    # url의 get으로 응답 가져오기
    
    if response.status_code == 200: # 응답의 응답코드
        html = response.text        # 응답의 html 코드
        soup = BeautifulSoup(html, 'html.parser')
    else:
        print('에러', response.status_code)
    
    # html의 코드 중 해당 태그 선별
    raw_article = soup.select(
        '#zone1 > div > div.newslist_wrap > div:nth-child(1) > ul > li'
    )
    
    # 선별된 태그들 정리해서 {제목, 날짜, url}을 리스트에 담기
    news_list = []
    
    for i, li_tag in enumerate(raw_article):
        
        dict = {}
        
        # 선별된 태그에서 다시 선별하여 text
        title = li_tag.select_one('a > div > span').text
        rdate = li_tag.select_one('a > div > div > span.date').text
        url   = li_tag.select_one('a').get('href')
        
        dict['key_title'] = title
        dict['key_rdate'] = rdate
        dict['key_url']   = url
        
        news_list.append(dict)
    
    news_list = str(news_list[:5])
    
    return news_list


def etf_list_json(url):
    
    """NAVER ETF 리스트 불러오기"""
    
    json_data = json.loads(requests.get(url).text)          # 불러온 url의 응답을 json 형태로 변환
    df = json_normalize(json_data['result']['etfItemList']) # json 형태를 df 형태로 변환
    
    etf_list = [] # ETF와 변동률을 담을 리스트
    
    for i in df.index:
        
        etf_dict = {}
        etf_dict['key_etf_name'] = df.loc[i, 'itemname']
        etf_dict['key_etf_rate'] = df.loc[i, 'changeRate']
        
        etf_list.append(etf_dict)
    
    return etf_list


# --------------------------------------------------

# 라우터 구성 : 해당 주소로 요청이 왔을 때 함수 호출
@app.route('/')
def index_copy():
    ytn_list = crawl('https://www.ytn.co.kr/news/list.php?mcd=0102')
    etf_list = etf_list_json('https://finance.naver.com/api/sise/etfItemList.nhn')
    
    # return render_template() : html 응답
    return render_template(
        'index_copy.html', # template 폴더 내 응답할 html 파일 경로
        MY_NAME='홍길동',   # html에서의 변수명 = flask의 변수명
        TEL='010-123', 
        MY_LIST=ytn_list,
        MY_ETF_LIST=etf_list,
    )

# --------------------------------------------------

# 서버 실행
if __name__ == '__main__':
    app.run(
        host='127.0.0.1', # 로컬 호스트, 루프백 주소
        port=8088,        # 임의로 할당가능
        debug=True,       # 변경이 감지될 때 재실행
    )