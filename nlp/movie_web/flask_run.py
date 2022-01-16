import pandas as pd
import numpy as np
from flask import Flask, make_response, jsonify, request, render_template
from bs4 import BeautifulSoup
import requests
import json
import xmltodict
from pandas.io.json import json_normalize
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                           #MY_LIST=ytn_list ,  #[{}]
                           )

if __name__ == '__main__':
    # ecos_openapi_xml()
    app.run(host='127.0.0.1', port=8088, debug=True)



#
# @app.route('/pykrx_ohlcv', methods=['POST'])
# def pykrx_openapi_df(limit_cnt=15):
#     krx_df = pd.read_csv("stock_12.csv")
#     print(krx_df.head())
#     # json_list = df.to_json()                        {"code":['111','222','333'], "price":['1000','2000','3000']}
#
#     krx_df = pd.merge(krx_df, list_df, how="left", on="종목코드")
#     # -------------------------------------------------------------
#     json_list = krx_df[:10].to_json(orient="values")  # [ ['111','222','333'], ['1000','2000','3000'] ]
#     # The return type must be a string, dict, tuple, Response instance,
#     json_obj = json.loads(json_list)
#     print(json_obj)                                  # [['111', '1000'], ['222', '2000'], ['333', '3000']]
#     ohlcv_html_str = json.dumps(json_obj)            # " [['111', '1000'], ['222', '2000'], ['333', '3000']] "
#     return ohlcv_html_str
#
# #---------------------------------------------
# # http://127.0.0.1:8088/go_rest3
# @app.route('/go_rest3', methods=['POST'])
# def rest3():
#     #<form>..<name="empno">
#     empno = request.form["empno"]
#     return "get11:  " + empno
# #---------------------------------------------
# # http://127.0.0.1:8088/go_rest4
# @app.route('/go_rest4', methods=['POST'])
# def rest4():
#     # $ajax()
#     # empno = request.form["empno"]
#     # return "ajax이보낸값:  " + empno
#     df  = pd.DataFrame({"code":['111','222','333'], "price":['1000','2000','3000']} )
#     # json_list = df.to_json()                    {"code":['111','222','333'], "price":['1000','2000','3000']}
#     json_list = df.to_json(orient="values")     # [ ['111','222','333'], ['1000','2000','3000'] ]
#     # The return type must be a string, dict, tuple, Response instance,
#     json_obj = json.loads(json_list)
#     print(json_obj)                             #    [['111', '1000'], ['222', '2000'], ['333', '3000']]
#     json_str = json.dumps(json_obj)             #  " [['111', '1000'], ['222', '2000'], ['333', '3000']] "
#     return json_str
