
import pandas as pd

df = pd.read_csv('./stock_12.csv')

df = df[['날짜', '시가', '고가', '저가', '종가', '거래량', '종목명', '종목코드']]

df = df.sort_values(['종목명', '날짜'])

df['변동률'] = round(df['종가'].pct_change(periods=1) * 100, 1)

def my_func(series):
    ss = round(series.pct_change(periods=1) * 100, 1)
    ss.fillna(method='bfill', inplace=True)
    return ss

df['변동률'] = df.groupby('종목코드')['종가'].apply(my_func)
# print(df.sort_values(['종목코드', '날짜']).head(30))

# list = df['종목코드'].unique().tolist()
# gb_df = df[(df['날짜'] >= '2020-12-01') & (df['날짜'] <= '2020-12-07')].groupby('종목코드')

# for i in list:
#     print(gb_df.get_group(i)[['날짜', '종목명', '종목코드', '변동률']])
# print(df[(df['날짜'] >= '2020-12-01') & (df['날짜'] <= '2020-12-07')].groupby('종목명').get_group('AJ네트웍스'), df.shape)

df_list = df.sort_values('날짜').groupby('종목코드')['변동률'].apply(lambda x: list(x))
mg = df[df['날짜'] == df['날짜'].max()]
df = pd.merge(mg, df_list, how='left', left_on='종목코드', right_on=df_list.index)[:15]
print(df)