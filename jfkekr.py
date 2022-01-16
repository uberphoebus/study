from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import roc_auc_score
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("./Quiz4/shipping.csv")
print(df.shape)
df.info()
df.head()
df.columns

df.select_dtypes()

df.isna().sum()

np.array().conc

from sklearn.model_selection import cross_val_score
scores = cross_val_score(X, y)
scores

X_train, X_test, y_train, y_test = train_test_split(X, y , test_size=0.2, random_state=1414, shuffle=True, stratify=y)
from sklearn.ensemble import BaggingClassifier
from xgboost import  XGBClassifier
from lightgbm import LGBMClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import StackingClassifier


X = pd.concat([X_train_scaler, X_test_scaler], axis=0)
y = pd.concat([y_train, y_test], axis=0)



X_trian, X_test, y_train, y_test = train_test_split(X,y , test_size=0.2, random_state=1414)
model = RandomForestClassifier()
model.fit(X_trian, y_train)
proba = model.predict_proba(X_test)
auc = roc_auc_score(y_test, proba[:, 1])
print(auc)

myparam = {"n_estimators":[300]}
gcv_model = GridSearchCV(model,param_grid=myparam, scoring='roc_auc', refit=True, cv=5)
gcv_model.fit(X,y)
print(gcv_model.best_score_)
print(gcv_model.best_params_)



