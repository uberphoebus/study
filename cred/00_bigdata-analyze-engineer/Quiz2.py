# -----------------------------------------------
# 구름devth (https://devth.goorm.io/)
# -----------------------------------------------

from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
from sklearn.model_selection import GridSearchCV
import warnings
warnings.filterwarnings(action='ignore')

#-----------------------데이터 로드 -------------------
X_train = pd.read_csv("./Quiz2/X_train.csv")
y = pd.read_csv("./Quiz2/y_train.csv")
X_test = pd.read_csv("./Quiz2/X_test.csv")
subdf = pd.DataFrame( {'cust_id':X_test.cust_id.values})
print(df.columns)


# ---------------df : X_train과 y_train 조인
# df = pd.merge([X_train, y_train], on='cust_id')


# -----------------------유니크 피쳐 삭제 -------------------
df.drop(['cust_id'], axis=1, inplace=True)
X_test.drop(['cust_id'], axis=1, inplace=True)

# -----------------------인코딩(결측처리+원핫)-------------------
# [['주구매상품','주구매지점']]

XX = pd.concat([X[['주구매상품','주구매지점']], X_test[['주구매상품','주구매지점']]], axis=0)
XX = pd.get_dummies(XX)                                                      #-------오타
X = pd.concat([X, Xdf.iloc[:df.shape[0],:]], axis=1)
X_test = pd.concat([X_test, Xdf.iloc[df.shape[0]:,:]], axis=1)

df.drop(['주구매상품','주구매지점'], axis=1, inplace=True)
X_test.drop(['주구매상품','주구매지점'], axis=1, inplace=True)

print(df.shape, y.shape, X_test.shape)   #(3500, 73) (2482, 73) (3500, 2)


#-----------------------결측처리----------------------------------
# 총구매액 = 최대구매액  + 환불금액
X['총구매액'].fillna(X['최대구매액'] + X['환불금액'], inplace=True)
X['최대구매액'].fillna(X['총구매액'] - X['환불금액'], inplace=True)
X['환불금액'].fillna(X['총구매액'] - X['최대구매액'], inplace=True)

X_test['총구매액'].fillna(X_test['최대구매액'] + X_test['환불금액'], inplace=True)
X_test['최대구매액'].fillna(X_test['총구매액'] - X_test['환불금액'], inplace=True)
X_test['환불금액'].fillna(X_test['총구매액'] - X_test['최대구매액'], inplace=True)


# #-----------------------로그&스케일링----------------------------------
# #log_cols = X[['총구매액','최대구매액','환불금액','내점일수','내점당구매건수','구매주기']]
for col in df.columns:                                                  #-------------- 오타
     log_arr = np.log1p(X[col].values)  		#array
     X[col] = log_arr.reshape(-1,1)

     log_arr = np.log1p(X_test[col].values)
     X_test[col] = log_arr.reshape(-1,1)

print(df.shape, y.shape, X_test.shape)   #(3500, 73) (2482, 73) (3500, 2)
df.fillna(0, inplace=True)
X_test.fillna(0, inplace=True)


scaler = StandardScaler()
scaler.fit(X)    #array matrics
X_scaler       = scaler.transform(X)
X_test_scaler = scaler.transform(X_test)

print(X_scaler.shape, y.shape, X_test_scaler.shape)   #(3500, 73) (2482, 73) (3500, 2)


#-----------------------학습&튜닝----------------------------------
model = RandomForestClassifier()
print(model.get_params())
myparam = {'n_estimators':[10], 'max_depth':[1] }  #,3,5]}                                     #-------오타
gcv_model = GridSearchCV(model, param_grid=myparam, cv=5, refit=True, scoring='accuracy')  #-------오타
gcv_model.fit(X_scaler, y)
print(gcv_model.cv_results_)
print(gcv_model.best_score_)   #-------오타
print(gcv_model.best_params_)
#
#
# # [ [0.67506762, 0.32493238],
# #   [0.67506762, 0.32493238],
# #   [0.66731487, 0.33268513]
# # ]
#
#
# # #-----------------------답안제출----------------------------------
# proba_list = gcv_model.predict_proba(X_test_scaler)      #-------오타
# print( np.array(proba_list).shape  )                     #--- (2482,3500)
# sub_df['gender'] = proba[:,1]  #.reshpae
# # #---------------------------------------------------------
# # check = pd.read_csv('sub_lkh.csv')
# # check.head()
#
#
