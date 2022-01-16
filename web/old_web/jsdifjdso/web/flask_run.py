#module name : flask_run.py

import pandas as pd
import numpy as np

# pip installl flask
from flask import Flask, make_response, jsonify, request, render_template

# pip install beautifulsoup4    -- 웹 크롤링
from bs4 import BeautifulSoup
import requests

# pip install pykrx             -- 주가정보 dataframe
from pykrx import stock
# pip install xmltodict         -- ecos xml 파싱
import json
import xmltodict
#                               -- ETF정보 json 파싱
from pandas.io.json import json_normalize
import datetime

app = Flask(__name__)

# http://www.naver.com
# http://www.naver.com/
# http://www.naver.com/index.html
# http://www.naver.com:80/index.html
# http://127.0.0.1:8088 /




def craw(url):
    #--------------- YTN 크롤링 ----------------
    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
    else:
        print("에러", response.status_code)

    #        python        html
    # ----  -------   --------------
    # 유일   #zone1   <id='zone1'>
    # 반복  .age      <class='age'>
    #zone1 > div > div.newslist_wrap > div:nth-child(1) > ul > li:nth-child(1)
    list = soup.select("#zone1 > div > div.newslist_wrap > div:nth-child(1) > ul > li")

    news_list = []
    for i, li_tag in enumerate(list):
        dict = {}
        title   = li_tag.select_one('a > div > span').text
        rdate   = li_tag.select_one('a > div > div > span.date').text
        url     = li_tag.select_one('a').get("href")
        # content = li_tag.select_one('a > div > div > span.desc').text

        dict['key_title'] = title
        dict['key_rdate'] = rdate
        dict['key_url'] = url
        # dict['key_content'] = content
        news_list.append(dict)
    news_list = news_list[:5]
    return news_list



def etf_list_json():
    url = 'https://finance.naver.com/api/sise/etfItemList.nhn'
    json_data = json.loads(requests.get(url).text)
    df = json_normalize(json_data['result']['etfItemList'])
    df = df[:15].copy()  # ----------------위에껀 API꺼 그냥 사용, 아래서 부터 가공
    etf_list = []
    for i in df.index:
        etf_dict={}
        etf_dict["key_etf_name"] = df.loc[i, 'itemname']
        etf_dict["key_etf_rate"] = df.loc[i, 'changeRate']
        etf_list.append(etf_dict)
    return  etf_list


@app.route('/pykrx_ohlcv', methods=['POST'])
def pykrx_openapi_df(limit_cnt=15):
    krx_df = pd.read_csv("stock_12.csv")
    print(krx_df.head())
    # json_list = df.to_json()                        {"code":['111','222','333'], "price":['1000','2000','3000']}
    json_list = krx_df[:10].to_json(orient="values")  # [ ['111','222','333'], ['1000','2000','3000'] ]
    # The return type must be a string, dict, tuple, Response instance,
    json_obj = json.loads(json_list)
    print(json_obj)                                  # [['111', '1000'], ['222', '2000'], ['333', '3000']]
    ohlcv_html_str = json.dumps(json_obj)            # " [['111', '1000'], ['222', '2000'], ['333', '3000']] "
    return ohlcv_html_str


# def pykrx_openapi_df(limit_cnt=15):
#     # 종목명	시가	고가	저가	종가	거래량
#     krx_df = pd.DataFrame(columns=['시가' ,'고가','저가','종가','거래량'])
#     tiker_list = stock.get_market_ticker_list("2021", market="KOSPI")  #KOSPI, KOSDAQ, KONEX
#     tiker_list = tiker_list[:limit_cnt]
#
#     print("----------------------call ------------------")
#     for i, ticker_code in enumerate(tiker_list):
#         ticker_name = stock.get_market_ticker_name(ticker_code)
#         print(ticker_code, ticker_name)
#
#         #시가 고가 저가 종가 거래량 날짜   +   종목코드 종목명
#         df = stock.get_market_ohlcv_by_date("20211001", "20211012", ticker_code)  #약2주 기간
#         df['종목명'] = ticker_name
#         df['종목코드'] = ticker_code
#         krx_df = pd.concat([krx_df, df], axis=0)
#         print(krx_df.shape)
#
#     krx_df = krx_df.reset_index().rename(columns={'index':'날짜'})
#     krx_df['날짜'] = krx_df['날짜'].astype('str')
#     krx_df = krx_df.sort_values('날짜')
#
#     krx_df.to_csv("krx_ohlcv.csv", index=False)
#
#
#     # json_list = df.to_json()                    {"code":['111','222','333'], "price":['1000','2000','3000']}
#     json_list = krx_df[:10].to_json(orient="values")  # [ ['111','222','333'], ['1000','2000','3000'] ]
#     # The return type must be a string, dict, tuple, Response instance,
#     json_obj = json.loads(json_list)
#     print(json_obj)  # [['111', '1000'], ['222', '2000'], ['333', '3000']]
#     ohlcv_html_str = json.dumps(json_obj)  # " [['111', '1000'], ['222', '2000'], ['333', '3000']] "
#     return ohlcv_html_str
#
#     # ----------------------------------------------------------------------------------
#     # strftime  : date2012-01-01 [datetime64]  --> str'2012-01-01' [object]
#     # strptime  : str'2012-01-01' [object]     --> date2012-01-01 [datetime64]
#     # krx_df["날짜"] = krx_df["날짜"].strftime("%Y-%m-%d")



def ecos_openapi_xml():
    url = "https://ecos.bok.or.kr/api/StatisticItemList/62TDLQ10E6ANSZGZB792/xml/kr/1/10/028Y015/"
    xml_string = requests.get(url).text
    json_string = json.dumps(xmltodict.parse(xml_string), indent=4)
    json_object = json.loads(json_string)
    row_list = json_object["StatisticItemList"]["row"]
    list = []
    for row in row_list:
        dict = {}
        dict['KEY_ITEM_NAME'] = row['ITEM_NAME']
        dict['KEY_DATA_CNT'] = row['DATA_CNT']
        list.append(dict)
    print(list[:3])
    return list


#---------------------------------------------
# http://127.0.0.1:8088/go_rest1?empno=7733
@app.route('/go_rest1', methods=['GET'])
def rest1():
    empno = request.args.get("empno") #?empno=7733
    return "get11:  " + empno
#---------------------------------------------
# http://127.0.0.1:8088/go_rest2?empno=1111
@app.route('/go_rest2', methods=['GET'])
def rest2():
    #<form>..<name="empno">
    # or  request.args.get("empno")
    empno = request.args["empno"]
    return "get22:  " + empno
#---------------------------------------------
# http://127.0.0.1:8088/go_rest3
@app.route('/go_rest3', methods=['POST'])
def rest3():
    #<form>..<name="empno">
    empno = request.form["empno"]
    return "get11:  " + empno
#---------------------------------------------
# http://127.0.0.1:8088/go_rest4
@app.route('/go_rest4', methods=['POST'])
def rest4():
    # $ajax()
    # empno = request.form["empno"]
    # return "ajax이보낸값:  " + empno
    df  = pd.DataFrame({"code":['111','222','333'], "price":['1000','2000','3000']} )
    # json_list = df.to_json()                    {"code":['111','222','333'], "price":['1000','2000','3000']}
    json_list = df.to_json(orient="values")     # [ ['111','222','333'], ['1000','2000','3000'] ]
    # The return type must be a string, dict, tuple, Response instance,
    json_obj = json.loads(json_list)
    print(json_obj)                             #    [['111', '1000'], ['222', '2000'], ['333', '3000']]
    json_str = json.dumps(json_obj)             #  " [['111', '1000'], ['222', '2000'], ['333', '3000']] "
    return json_str


#---------------------------------------------
@app.route('/ajax_test_html')
def ajax_test_html():
    return render_template('ajax_test.html')
#---------------------------------------------

@app.route('/')
def index():
    # if request.method == "POST":
    #     limit_cnt = request.form["MY_LIMIT_CNT"]
    # else:
    #     limit_cnt = 15

    ytn_list = craw("https://www.ytn.co.kr/news/list.php?mcd=0102")
    etf_list = etf_list_json()
    return render_template('index.html',
                           MY_NAME='홍길동',
                           MY_LIST=ytn_list ,
                           MY_ETF_LIST= etf_list,
                           TEL="010-123"
                          # **MY_DICT
                           )  #url, **  id=kim, pw=11 , addr=s


# # http://127.0.0.1:8088  /abc
# @app.route('/abc')
# def okabc():
#     myprint()
#     return 'abc!'
#
# def myprint():
#     print("ddd")

if __name__ == '__main__':
    # ecos_openapi_xml()
    app.run(host='127.0.0.1', port=8088, debug=True)