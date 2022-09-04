# 210817_lec

import numpy as np
import pandas as pd


# sql insert, update, delete
# df; [] () {} array Series



#-------------------
#2. numpy reshape
#-------------------
import numpy as np

df = pd.DataFrame(data=eng_score, columns=['eng'])
mat_score = [66,77,88,]

mat_array = np.array(mat_score)   #[66 77 88 ]  list-->array
mat_array = mat_array.reshape(-1, 1)
print(mat_array, type(mat_array))

mat_list = mat_array.tolist()    #list-->array
print(mat_list, type(mat_list))


df['mat'] = mat_array
print(df.head())

# score = [[10,20,30,],  [66,77,88,]]
# df = pd.DataFrame(data=score) #, columns=['eng'])
# print(df.head())

dict = {"kor":[10,20,30], "eng":[55,66,77]}
df = pd.DataFrame(dict)
print(df.head())

# ----------------------------------------
# insert
# ----------------------------------------


eng = [10, 20, 33]
a = pd.DataFrame(data=eng, columns=['eng']) # 한개 리스트는 srs
a['math'] = [20, 50, 60]

data = [[10, 20, 40], [55, 77, 88]] # 리스트로 묶으면 행 단위
a = pd.DataFrame(data=data)

math = [20, 66, 88]
# srs로 합치는 방법
# a = pd.Series([eng, math], keys=['eng', 'math'])

df = pd.DataFrame(data=eng, columns=['eng'])
# a = pd.concat([a, math], axis=1)

# np reshape로 합치는 방법
a = pd.DataFrame(data=eng, columns=['eng'])
math_array = np.array(math)
math_array = math_array.reshape(-1, 1)
a['math'] = math_array
# reshape(3, 2); 3행 3열로 변경

# array -> list
a = math_array.tolist()

# dict
dict = {'name':['aa', 'bb', 'cc'], 'kor':[10, 20, 30], 'eng':[55, 66, 77], 'math':[np.nan, 100, 100]}
df = pd.DataFrame(dict)

# df 값 수정; lambda, repalce, apply

# null 검사
print(df.isna().sum())

# null 채우고 덮어쓰기
print(df.fillna(0, inplace=True))


# np.nan이 들어가면 float
print(df.info())

# df에 srs 추가하기
# pd.concat([df, srs], axis=1, keys=['eng', 'math'])
# 혹은 컬럼설정; df.columns = ['eng', 'math']

# srs, srs 병합
eng_score = [10, 20, 30]
mat_score = [66, 77, 88]
es = pd.Series(eng_score)
ms = pd.Series(mat_score)
df = pd.concat([es, ms], axis=1 ,keys=['eng', 'math'])
df.columns = ['eng', 'math']
print(df)


# ----------------------------------------
# update; lambda
# ----------------------------------------

# lambda _input_ : _return_
def squ(x):
    return x * 3
print(squ(4))

lambda_def = lambda x: x * 3
print(lambda_def(4))

dict = {'name':['aa', 'bb', 'cc'], 'kor':[10, 20, 30], 'eng':[55, 66, 77], 'math':[np.nan, 100, 100]}
df = pd.DataFrame(dict)
df.fillna(0, inplace=True)
print(df)

# eng > 70 a, eng > 60 b, eng > 50 c

def grade_add(eng):
    if eng > 70:
        grade = 'a'
    elif eng > 60:
        grade = 'b'
    else:
        grade = 'c'
    return grade

print(grade_add(43))

# lambda; .apply 앞의 데이터를 input
df['grade'] = df['eng'].apply(lambda x: grade_add(x))
print(df)

# math 100 P, else F
def math_pf(math):
    if math == 100:
        grade2 = 'P'
    else:
        grade2 = 'F'
    return grade2

df['grade2'] = df['math'].apply(lambda x: math_pf(x)); print(df)

# .apply(lambda)
df['grade3'] = df['math'].apply(lambda x: 'p' if x == 100 else 'f'); print(df)

# ----------------------------------------
# delete
# ----------------------------------------

# cols delete
df = df.drop('grade3', axis=1); print(df)

# list 형태도 가능
del_cols = ['grade', 'grade2']
df = df.drop(del_cols, axis=1); print(df)

# rows delete; idx
df = df.drop(index=2, axis=0); print(df)

# ----------------------------------------
# update; replace
# ----------------------------------------

df = df.replace('aa', 'aaa'); print(df)

# aa; 30, 20, 50 추가
row = ['aa', 30, 20, 50]
df.loc[2] = row; print(df)

df.replace('aa', 'aaa', inplace=True); print(df)

# 특정 값 수정
# 데이터량이 많을 때 at, iat이 빠름
# 공모전에서는 메모리 사용량, 퍼포먼스 등도 고려 대상
print(df.iloc[2, 2])
print((df.loc[2, 'eng']))
print(df.iat[2, 2])
print(df.at[2, 'eng'])


# ----------------------------------------
# module name; lec02_titanic.py
# ----------------------------------------

"""
ML; 학습거리를 스스로 학습하는 인공지능
ML 구조; 입력 -> 특징 추출 -> 분류 -> 출력
DL 구조; 입력 -> 블랙박스 -> 출력
ML은 인간 개입 가능
지도학습 vs 비지도학습(supervised vs unsup); label
지도학습; train-set(학습데이터)과 정답(실제값, label)이 있음, loss를 비교할 수 있는
비지도학습; label이 없고 loss가 없음

지도학습은 다시 회귀/분류로 나누고, 비지도는 군집
지도학습이 80%, 비지도학습은 20% 비중
모든 공모전은 점수를 내야하기 때문에 지도학습(label)
비지도학습의 예; 고객데이터 segmentation

분류 4-5일, 회귀 2-3일, 군집 1-2일; 총 2주 소요

대부분 공모전 최대 3인
자발적으로 참가 가능

회귀; 연속적 숫자, 실수를 예측
분류; 정의된 label 중 하나 예측, 이진/다중 분류
같은 모델로도 회귀, 분류 모델을 만들 수 있음
가설에 의해 회귀, 분류가 정해지기 때문에 정해야 함

sql의 테이블 == frame
sql의 컬럼 == feature
sql의 데이터, 레코드 == data set
sql의 rows, cols (1000 * 5) == (1000 * 5)

머신러닝에서 데이터 전체를 다루는 일은 적음
일반적으로 7:3, 8:2, 9:1로 나눔
나눈 7, 8, 9를 학습데이터, training data set
3, 2, 1을 test data set

나누는 이유는 테스트를 해보기 위함

비지도변환; 군집 label이 없음
분류와 군집의 가장 큰 차이는 label 유무

overfitting 과대적합; 학습만 잘돼서 검증이 어려움
과대적합 예; 분류가 없는 생소한 데이터가 있을 때 분류를 못해냄
생소한 데이터에 대한 대비; 데이터 인사이트
underfitting 과소적합; 데이터량이 부족한 경우

일반화; 학습과 예측이 모두 잘 되는 경우


1. problem def
2. problem feature; 가장 중요한 부분
3. select framework; 대부분 공모전에는 여기까지 주어짐
# 파이널에서 개인 소비 데이터 사용 불가(개인정보 관련)

4. eda; 데이터 정리, 분포, 모양새, feature 간 관계
5. feature engineering; str -> int, null, 고유번호 제거, 데이터 정제/가공
# 인간 개입이 들어가는 부분

6. model selection; 알고리즘 선정
7. apply learning
8. model maintenance

1~8 과정 반복; 유지보수

신입은 2~4부터 업무 시작; 8개월
가공은 1개월. 정해져 있는 부분
모델 선정도 경험적으로 정해져 있음. 1~2개월

데이터 전처리, 가공이 80%; 신입 업무 부분

eda, engineering이 가장 중요한 부분
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
print(sklearn.__version__)

# import warning ignore

# 이상값; 정규분포 유의검증 수준 밖의 값
# 이상값은 분석가 정하기 나름
# 인코딩; 글자를 숫자화

# titanic eda

# 1. 문제정의; 캐글 문제, train을 통해 test 대조하여 생존 예측
# https://www.kaggle.com/c/titanic/overview

# passenderid; 제거 대상
# ss; 형제자매, 배우자
# parch; 부모, 자식
# ticket; 확인 필요
# fare; sibsp/parch 합산 요금
# embarked; 승선 장소 코드 번호


# pd.read_csv('./') ; 현재 폴더 의미 ./
train = pd.read_csv('./kaggle/01_titanic/input/train.csv')
test = pd.read_csv('./kaggle/01_titanic/input/test.csv')
submission = pd.read_csv('./kaggle/01_titanic/input/gender_submission.csv')

# eda

# 1. 형태 확인; shape, info
print(train.shape), print(test.shape)
print(train.info())
# encoding; Name, Sex, Ticket, Cabin, Embarked

# 2. data 확인; 절대 전체를 불러오지 말 것
print(train.head())
print(train.tail())

# 3. target label 확인; 분포, 값
# balanced; 데이터가 고르게 분포된 경우
# inbalanced; 타겟이 극소수인 경우
print(train['Survived'].value_counts())

a = train.shape[0]
b = train[train.Survived == 0]['Survived'].count()
c = train[train.Survived == 1]['Survived'].count()
print(b / a * 100)
print(c / a * 100)

# 4. missing value
# 채울 결측치; Age 177, Cabin 687, Embarked 2, Fare 1
print(train.isna().sum())
print(test.isna().sum())

# df1.append(df2); 가장 간편
train_test = train.append(test)
print(train_test.shape)
print(train_test.isna().sum())
print(train_test.isna().sum() / train_test.shape[0] * 100)

# 공통적으로 사용할 함수
def nan_check():
    nan_dict = {'CNT':train_test.isna().sum(),
                'RATE':train_test.isna().sum() / train_test.shape[0] * 100}
    nan_df = pd.DataFrame(nan_dict)
    return nan_df.head().T

print(nan_check())

# 1. encoding; object to numeric
# name     ; mr. miss.
# Sex      ; 1 / 0
# Ticket   ; drop
# Cabin    ; A ~ E (구역번호와 위치)
# Embarked ; 0 / 1 / 2

# 2. missing val; Age 177, Cabin 687, Embarked 2, Fare 1

# feature engineering(가공); encoding & missing val
# eda, fe 순서는 무관

# 대략적 시각화; 수치형만 가능, 가득 찬 차트는 고유값
train_test.hist()
# print(plt.show())

# 3. 정규분포화/표준화; 왜도/첨도 제거
# 왜도; 정규분포 쏠린 정도, 좌우 치우침
# 첨도; 정규분포가 뾰족한 정도, 중앙값 부근으로 값이 밀집

# 4. 스케일링; 값의 지수화, 수치 맞추기
# 같은 기준으로 비교하기 위함

# 5. 이상값(outlier) 처리

# 6. 파생변수; family = Sibsp + Parch 후 drop

# 7. category; 구간화(바인딩), 연령 등

# 1. encoding의 두 방법
# 1) encoding
# 2) one hot encoding; 1/0으로 변환, 컬 럼수 증가, 위계 개념이 사라짐
# 3) get_dummmy(); 1) 2) 모두 수행, df 전체에서만 사용 가능
# 4) map(), apply(), lambda
# 큰 수치는 좋은 값으로 인식

# 2. missing val
# df.fillna(0, inplace=True)
# Age; 호칭에 대한 평균값을 나이 결측치에 부여
# Cabin; 너무 많은 결측치, 50% 이상이면 일반적으로 drop
# Embarked; 최빈값 부여
# Fare; 동행자 수, pclass가 유사한 데이터의 평균


# pd.get_dummies()
# prefix; 앞에 붙일 별칭
# drop_first = True; 변환 전 값 drop
# 필요한 부분만 해야 양질의 df 구성
# 구간화; 10대, 20대, 30대 등
# 구간화 후 get_dummies
print(train_test.shape)
# train_test = pd.get_dummies(train_test)
print(train_test.shape)
print(train_test.head())
print(train_test.describe())

# 공백처리
train_test['Cabin'].fillna('U0', inplace=True)
print(train_test['Cabin'].str[0:1].value_counts())

# cabin과 생존의 상관관계 확인
train_test['Cabin'] = train_test['Cabin'].str[0:1]
train['Cabin'] = train['Cabin'].str[0:1]
cross = pd.crosstab(train['Cabin'], train['Survived'])
print(cross)

cross = pd.crosstab(train['Cabin'], train['Pclass'])
print(cross)

# inplace=True는 return이 없음, 원본을 수정
# 따라서 함수를 추가적으로 적용할 수 없음
# NoneType은 return이 없다고 의심해볼 수 있음

drop_cols = ['PassengerId', 'SibSp', 'Parch', 'Ticket', 'Cabin']
# train_test.drop(drop_cols, axis=1, inplace=True)