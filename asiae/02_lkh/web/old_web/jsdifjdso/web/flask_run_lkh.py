#module name : flask_run.py
# pip installl flask

from flask import Flask, make_response, jsonify, request, render_template

app = Flask(__name__)

# http://www.naver.com
# http://www.naver.com/
# http://www.naver.com/index.html
# http://www.naver.com:80/index.html
# http://127.0.0.1:8088 /

from bs4 import BeautifulSoup
# pip install beautifulsoup4
import requests



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


@app.route('/')
def index():
    ytn_list = craw("https://www.ytn.co.kr/news/list.php?mcd=0102")

    MY_DICT = {"ADDR": "서울", "TEL": "010-123"}
    return render_template('index.html',
                           MY_NAME='홍길동',
                           MY_LIST=ytn_list ,
                           ADDR="서울",
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
    print("main 실행")
    app.run(host='127.0.0.1', port=8088, debug=True)