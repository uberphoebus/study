
import numpy as np
import pandas as pd

# --------------------------------------------------
# 1. list --> dataframe
# pd.DataFrame(data=list, columns=[])
# --------------------------------------------------
eng_score = [10, 20, 30]
df = pd.DataFrame(data=eng_score, columns=['eng'])
print(df.head())

# --------------------------------------------------
# 2. df + srs
# pd.concat([df, srs], axis=1), df.columns = []
# --------------------------------------------------
mat_score = [66, 77, 88]
ms = pd.Series(mat_score)
df = pd.concat([df,ms], axis=1)
df.columns = ["eng", "math"]
print(df.head())

# --------------------------------------------------
# 3. srs + srs
# pd.concat([srs, srs], axis=1), df.columns = [] ; axis=1 cols
# --------------------------------------------------
es = pd.Series(eng_score)
ms = pd.Series(mat_score)
df = pd.concat([es, ms], axis=1)
df.columns = ['eng', 'math']
print(df)

# --------------------------------------------------
# 4. numpy reshape & tolist
# np.array(list), array.reshape(a, b) ; a rows, b cols
# array.tolist()
# --------------------------------------------------
df = pd.DataFrame(data=eng_score, columns=['eng'])
mat_array = np.array(mat_score)
mat_array = mat_array.reshape(-1, 1)
print(mat_array, type(mat_array))

mat_list = mat_array.tolist()
print(mat_list, type(mat_list))
df['mat'] = mat_array; print(df.head())

# --------------------------------------------------
# 5. dict --> df
# pd.DataFrame(dict)
# --------------------------------------------------

dict = {'name':['aa', 'bb', 'cc'], 'kor':[10, 20, 30], 'eng':[55, 66, 77], 'math':[np.nan, 100, 100]}
df = pd.DataFrame(dict); print(df.head())

# --------------------------------------------------
# 6. null
# .isna().sum(), .fillna(), np.nan
# inplace=True ; 덮어쓰기, return 없음
# np.nan 입력되면 컬럼 데이터 타입 float
# --------------------------------------------------

print(df.isna().sum())
print(df.fillna(0, inplace=True))
print(df.info())

# --------------------------------------------------
# 7. lambda
# lambda _input_: return if cond else return
# input_df.apply(func)
# --------------------------------------------------

def squ(x):
    return x * 3
print(squ(4))

squ_lamb = lambda x: x * 3
print(squ_lamb(4))

def grade_add(eng):
    if eng > 70:
        grade = 'a'
    elif eng > 60:
        grade = 'b'
    else:
        grade = 'c'
    return grade

print(grade_add(43))

# lambda
df['grade'] = df['eng'].apply(lambda x: grade_add(x))
print(df.head())

def math_pf(math):
    if math == 100:
        grade = 'P'
    else:
        grade = 'F'
    return grade

df['grade2'] = df['math'].apply(lambda x: math_pf(x))
df['grade3'] = df['math'].apply(lambda x: 'p' if x == 100 else 'f')
print(df.head())

# --------------------------------------------------
# 8. drop(delete)
# df.drop(cols, axis=1)
# df.drop(index=, axis=1)
# --------------------------------------------------

df = df.drop('grade3', axis=1) # cols drop
print(df.head())

del_cols = ['grade', 'grade2'] # cols list drop
df = df.drop(del_cols, axis=1)
print(df.head())

df = df.drop(index=2, axis=1)  # rows drop
print(df.head())

# --------------------------------------------------
# 9. replace
# df.replace(vl1, vl2)
# .loc/at[] = vl
# .at/iat[] 사용 권장
# --------------------------------------------------
df = df.replace('aa', 'aaa') # df내 전체 값 수정
print(df)

row = ['aa', 30, 20, 50]
df.loc[2] = row              # rows 추가
print(df)

# --------------------------------------------------
# AI, ML, DL intro
# --------------------------------------------------

# ml; 학습 내용이 주어지면 스스로 학습하는 AI
#
# ml구조; 입력 -> 특징 추출(인간 개입) -> 분류 -> 출력
# dl구조; 입력 -> 블랙박스 -> 출력
#
# 지도학습(supervised); 회귀, 분류 / label, loss
# 비지도학습(unsup); 군집(고객 segmentation)
#
# 회귀; 연속적 숫자, float 예측
# 분류; label 예측, 이진/다중 분류
# 군집; label 없음
#
# db = table, cols,    records,  (rows, cols)
# da = frame, feature, data set, (rows, cols)
#
# training data set : test(검증) data set = 7:3 or 8:2
#
# 과대적합; 일반화가 어려운 경우
# 과소적합; 학습데이터가 적은 경우
# 일반화; 정확하게 예측할 경우
#
# 1. problem def
# 2. problem feature; 가장 중요
# 3. select frameworkd; 대부분 3단계까지 주어짐
# 4. eda; 분포, 형태, feature 관계
# 5. feature engineering; encoding 등 데이터 정제/가공
# 6. modle selection; 알고리즘 선정, 경험적 자료 많음
# 7. apply learning
# 8. model maintenance

# --------------------------------------------------
# titanic EDA
# --------------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
print(sklearn.__version__)

train = pd.read_csv('./kaggle/01_titanic/input/train.csv')
test = pd.read_csv('./kaggle/01_titanic/input/test.csv')
submission = pd.read_csv('./kaggle/01_titanic/input/gender_submission.csv')

# --------------------------------------------------
# 가공/정제 전 확인
# 1. 형태; .shape, .info()
# 2. data; .head(), .tail()
# 3. missing value; .isna().sum()
# 4. target label; .value_counts() balanced/inbalanced
# 5. train, test 동일하게 정제
# --------------------------------------------------
print(train.shape), print(test.shape), print(train.info())
# need encoding; Name, Sex, Ticket, Cabin, Embarked

print(train.head()), print(train.tail())

print(train.isna().sum()), print(test.isna().sum())
# missing val; Age 177, Cabin 687, Embarked 2, Fare 1

# missing val func
def nan_check():
    nan_dict = {'CNT':train_test.isna().sum(),
                'RATE':train_test.isna().sum()
                       / train_test.shape[0] * 100}
    nan_df = pd.DataFrame(nan_dict)
    return nan_df.head().T

print(train.Survived.value_counts())
# target label 분포; balanced

rows = train.shape[0]
surv_count = train[train['Survived'] == 0]['Survived'].count()
dead_count = train[train['Survived'] == 1]['Survived'].count()
print(surv_count / rows * 100), print(dead_count / rows * 100)

# train, test append/concat
train_test = train.append(test)
print(train_test.shape), print(train_test.isna().sum())

# --------------------------------------------------
# EDA procedure
# 1. feature engineering; encoding, missing val
# 2. 대략적 시각화
# 2. 표준화(정규분포화); 왜도, 첨도 제거
# 3. 스케일링
# 4. outlier(이상값) 처리
# 5. 파생변수 설정
# 6. binding(구간화)
# --------------------------------------------------

# --------------------------------------------------
# 1. 대략적 시각화
# 수치형만 가능, 가득 찬 차트 형태는 고유값일 때
# --------------------------------------------------
print(train_test.shape), print(train_test.isna().sum())
print(train_test.describe())
train_test.hist()
# print(plt.show()) # pycharm에서 시각화 출력

# --------------------------------------------------
# 2. missing val; Age 263, Cabin 1014, Embarked 2, Fare 1
# df.fillna(0, inplace=True)
# Age      ; 호칭의 평균값 활용
# Cabin    ; drop. 50% 이상 결측치
# Embarked ; 최빈값 활용
# Fare     ; 유사한 동행자수, pclass 데이터의 평균 활용
# --------------------------------------------------
train_test['Cabin'].fillna('U0')               # return 있음
train_test['Cabin'].fillna('U0', inplace=True) # return 없음
print(train_test['Cabin'].str[0].value_counts())
# NoneType; inplace는 return이 없으므로 함수를 추가적으로 적용할 수 없음

train_test['Cabin'] = train_test['Cabin'].str[0]
train['Cabin'] = train['Cabin'].str[0]
cross_s = pd.crosstab(train['Cabin'], train['Survived'])
cross_p = pd.crosstab(train['Cabin'], train['Pclass'])
print(cross_s), print(cross_p)

drop_cols = ['PassengerId', 'SibSp', 'Parch', 'Ticket', 'Cabin']
# train_test.drop(drop_cols, axis=1, inplace=True)

# --------------------------------------------------
# 3. encoding; object to numeric
#    1) encoding
#    2) one hot encoding; 위계 제거, 컬럼수 증가
#    3) get_dummies(); 1) + 2)
#    4) map(), apply(), lambda
# Name(mr. miss.), Sex(1/0), Ticket(drop), Cabin(A~E), Embarked(0/1/2)
# --------------------------------------------------

# --------------------------------------------------
# 4. 표준화(정규분포화)
# 왜도; 분포가 좌우로 치우친 정도
# 첨도; 분포가 중앙값 부근으로 밀집된 정도
# --------------------------------------------------

# --------------------------------------------------
# 5. 스케일링
# 같은 기준으로 다른 값들을 상대적으로 비교
# --------------------------------------------------

# --------------------------------------------------
# 6. outlier(이상값) 처리
# --------------------------------------------------

# --------------------------------------------------
# 7. 파생변수; 유사한 데이터를 결합한 변수
# family = SibSp + Parch
# -------------------------------------------------

# --------------------------------------------------
# 8. binding(구간화)
# encoding(get_dummies())을 위해 연령 등을 구간으로 나눔
# --------------------------------------------------
