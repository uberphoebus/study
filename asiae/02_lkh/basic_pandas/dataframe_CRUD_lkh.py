

# [] () {} array Series
import pandas as pd

df = pd.concat([df2,s], axis=1)

#-------------------
#1. list --> dataframe
#-------------------
eng_score = [10,20,30,]
df = pd.DataFrame(data=eng_score, columns=['eng'])
print(df.head())

#-------------------
#2. dataframe + series
#-------------------
mat_score = [66,77,88,]
ms = pd.Series(mat_score)
df = pd.concat([df,ms], axis=1)  #, keys=["eng","math"])
df.columns = ["eng", "math"]
print(df.head())

#-------------------
#1. series + series
#-------------------
eng_score = [10,20,30,]
mat_score = [66,77,88,]

es = pd.Series(eng_score)
ms = pd.Series(mat_score)
df = pd.concat([es, ms], axis=1 , ignore_index=True)
df.columns = ["eng","math"]
print(df.head(10))


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


#--------------------------
# update
#--------------------------
dict = {"name":['aa','bb','cc'], "kor":[10,20,30], "eng":[55,66,77], "mat":[np.nan, 100,100]}
df = pd.DataFrame(dict)
print(df.head())
print(df.info())


#--------------------------
# update : 결측처리
#--------------------------
print(df.isna().sum())  #nan 검사
df = df.fillna(0)       #nan 채우기
df.fillna(0, inplace=True)
print(df.head())

#--------------------------
# update : lambda
#--------------------------
def squ(x) :
    return x*3

res = squ(4)
print(res)

lambda_def = lambda x : x*3
print(lambda_def(4))


def grade_add(eng) :
    grade = "a"
    if eng > 70:
        grade = "a"
    elif eng > 60 :
        grade = "b"
    else :
        grade = "c"
    return grade

print(grade_add(80))
df["grade"] = df["eng"].apply(lambda x : grade_add(x))  #df["eng"]
print(df.head())


def math_pf(math):
    grade = "P"
    if math == 100:
       grade = "P"
    else:
       grade = "F"
    return grade
df["grade2"] = df["mat"].apply(lambda x : math_pf(x))  #df["eng"]
df["grade3"] = df["mat"].apply(lambda x : "P" if x==100  else "F")
print(df.head())


#-------------
# delete
#-------------
# df.drop("grade3", axis=1, inplace=True)
df = df.drop("grade3", axis=1)
print(df.head())

del_cols = ["grade", "grade2"]
df = df.drop(del_cols, axis=1)
print(df.head())

# delete from emp where empno=7733
df = df.drop(index=2, axis=1)
print(df.head())

#-------------
# update : replace
#-------------
row = ['aa', 30,20,50]
# df = df.append(pd.Series(row, name=10))
# df = df.append(pd.Series(row), ignore_index=True)
# df = df.append(pd.Series(row, index=df.columns), ignore_index=True)
df.loc[2] = 0
df.loc[2] = row
print(df.head())

# update emp set name='aaa' where name='aa';
df = df.replace('aa', 'aaa') #, inplace=True)
print(df.head())

# update emp set name='aaaa' where key='0';
print(df.iloc[2, 2])     #행번째, 열번째
print(df.loc[2, "eng"])  #인덱스값, 컬럼명
    # df.ix(2, "eng") -- XXXXXX
print(df.iat[2,2])
print(df.at[2, "eng"])


