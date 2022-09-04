from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np

df = pd.read_csv("./Quiz1/mtcars.csv")
scaler =  MinMaxScaler()
matrix = scaler.fit_transform(df['qsec'].values.reshape(-1,1))      #array , matrix
df['qsec_mm'] = matrix
print(len(df[df['qsec_mm']>0.5].index))
# print(df[df['qsec_mm']>0.5]['qsec_mm'].count())

