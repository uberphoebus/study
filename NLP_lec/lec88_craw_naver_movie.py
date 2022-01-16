import sqlalchemy as sa
import cx_Oracle
import xml.etree.ElementTree as ET
import json
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import datetime
import random
random.uniform(0.2, 1.2)

oracle_engine = sa.create_engine('oracle://conf:0000@localhost:1521/xe')
def craw_movie(pageno=None):
    with oracle_engine.connect() as conn:
        trans = conn.begin()

        # for pageno in range(1,400,1):
        for pageno in range(1, 1000, 1):
            url = 'https://movie.naver.com/movie/point/af/list.naver?&page=' + str(pageno)
            print(url)
            response = requests.get(url)

            interval = round(random.uniform(0.2, 1.2), 2)
            time.sleep(interval)

            if response.status_code == 200:
                html = response.text
                soup = BeautifulSoup(html, 'lxml')

                review_list  = []
                trs = soup.select('div#old_content > table > tbody > tr')
                for td in trs:
                    review_dict={}
                    title = td.select_one('td.title > a.movie.color_b').text
                    score = td.select_one('td.title > div > em').text
                    review = td.select_one('br').next_sibling.strip()
                    review_dict['title']  = title
                    review_dict['score']  = score
                    review_dict['review'] = review
                    review_list.append(review_dict)
                    try:
                        sql = "insert into craw_naver_movie2(seq, title, score, review) values (craw_naver_movie_seq.nextval,  :2, :3, :4)"
                        conn.execute(sql, (title, score, review))
                    except Exception as e:
                        continue
                        # trans.rollback()
                        # print(e)
                        print("에러발생")
            else:
                print("에러발생" + response.status_code)

        trans.commit()
    return review_list

# review_list = craw_movie()
# print(review_list[:5])



# from sqlalchemy import types, create_engine
# oracle_engine = create_engine('oracle://conf:0000@localhost:1521/XE')
# sql = "select title,score, review from naver_movie"
# df = pd.read_sql_query(f'''{sql}''', oracle_engine)
# print(df.head())
# df.to_csv("./datasets/naver_review.csv", index=False)