import pandas as pd
import numpy as np

df = pd.read_csv("stock_12.csv")
print(df.columns.tolist())

df = df[['날짜', '시가', '고가', '저가', '종가', '거래량', '종목코드', '종목명']]
df.to_csv("stock_12.csv", index=False)
print(df.head())

# stock = pd.read_csv("stock_ohlcv_v01.csv")
#
# info = pd.read_csv("iem_info_20210902_utf8.txt")
# info["iem_cd"] = info["iem_cd"].str[1:]
#
# print(info.head())
# print(stock.head())
#
# df = pd.merge(stock, info, left_on='종목코드' , right_on='iem_cd')
# df.drop(['iem_cd', 'btp_cfc_cd', 'mkt_pr_tal_scl_tp_cd', 'stk_dit_cd'], axis=1, inplace=True)
# df = df[[ '시가', '고가', '저가', '종가', '거래량', '일자', '종목코드', 'iem_krl_nm']]
# df.columns = [ '날짜', '시가', '고가', '저가', '종가', '거래량', '종목코드', '종목명']
# df = df.sort_values('날짜')
#
# df = df[(df['날짜']>='2020-12-01') & (df['날짜']<='2020-12-31')].sort_values(['날짜', '종목명'])
# df.to_csv("stock_12.csv", index=False)
# print(df.head(), df.shape)


