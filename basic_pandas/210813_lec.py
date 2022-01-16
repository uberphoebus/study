'''
df화 방법들
1. 리스트를 넣기
2. csv 읽어오기

'''

# module name; lec_01.py
# df; list tuple dict

mlist = [[1, 2], 3, 'abc', [55, 66, [777, 888]]]

for i, a in enumerate(mlist):
    i, a

a = mlist[3][2][0]

dict = [{'id':'kim', 'pw':111, 'addr':'서울'},
        {'id':'hong', 'pw':222, 'addr':'경기도'}]
a = dict[0]['addr']

for i, val in enumerate(dict):
    i, val

# print(dict[1]['id'])

ytb_res = {
 "kind": "youtube#videoListResponse",
 "etag": "\"UCBpFjp2h75_b92t44sqraUcyu0/sDAlsG9NGKfr6v5AlPZKSEZdtqA\"",
 "videos": [
  {
   "id": "7lCDEYXw3mM",
   "kind": "youtube#video",
   "etag": "\"UCBpFjp2h75_b92t44sqraUcyu0/iYynQR8AtacsFUwWmrVaw4Smb_Q\"",
   "snippet": {
    "publishedAt": "2012-06-20T22:45:24.000Z",
    "channelId": "UC_x5XG1OV2P6uZZ5FSM9Ttw",
    "title": "Google I/O 101: Q&A On Using Google APIs",
    "description": "Antonio Fuentes speaks to us and takes questions on working with Google APIs and OAuth 2.0.",
    "thumbnails": {
     "default": {
      "url": "https://i.ytimg.com/vi/7lCDEYXw3mM/default.jpg"
     },
     "medium": {
      "url": "https://i.ytimg.com/vi/7lCDEYXw3mM/mqdefault.jpg"
     },
     "high": {
      "url": "https://i.ytimg.com/vi/7lCDEYXw3mM/hqdefault.jpg"
     }
    },
    "categoryId": "28"
   },
   "contentDetails": {
    "duration": "PT15M51S",
    "aspectRatio": "RATIO_16_9"
   },
   "statistics": {
    "viewCount": "3057",
    "likeCount": "25",
    "dislikeCount": "0",
    "favoriteCount": "17",
    "commentCount": "12"
   },
   "status": {
    "uploadStatus": "STATUS_PROCESSED",
    "privacyStatus": "PRIVACY_PUBLIC"
   }
  }
 ]
}

# 이 형태의 데이터를 꺼내오기 위해 l, t, d 학습
# print(ytb_res['videos'][0]['snippet']['thumbnails']['default']['url'])

# kakao rest api json
# python에서는 dict, css에서는 json 등 이름만 다르지 형태는 같음
kakao_res = {
  "successful_receiver_uuids": ["abcdefg0001","abcdefg0002"],
  "failure_info":[{
      "code": -532,
      "msg": "daily message limit per sender has been exceeded.",
      "receiver_uuids": ["abcdefg0003"]
  }]
}
# print(kakao_res['failure_info'][0]['receiver_uuids'][0])

# 데이터 수집 방법
# 1. API 가입해서 요청; 공공데이터포털, dart, 파이낸셜, 카카오, 유튜브 등
# 2. 크롤링
# 3. 구매
# 4. 자체 데이터

# cd venv 로 터미널 경로 설정 가능

# 해당 분야의 도메인(기반지식)이 있어야 함
# 데이터 분석가는 가공을 잘하는 것이 아니라,
# 도메인을 갖고, AI에 넣을 수 있는 데이터를 선별할 수 있는 능력
# 데이터 사이언티스 신입 공고는 데이터 가공 정도의 업무
# 모델 찾는 법, 튜닝하는 방법도 알아야 함
# 그러나 현업에서는 다룰 수 없음

# v는 변수, __는 예약된 기능
# f는 pd에서 제공되는 함수. 동사(행위)
# c는 class; 함수와 변수를 한 바구니에 넣어두는 것
# 클래스 내에만 self가 있고 내부적으로 주소를 알아서 찾음
# from ~ 모듈(. 앞은 폴더) selenium.webdriver.common.keys
# import ~ 클래스 or 메서드
# 폴더 > 모듈 > 클래스 > 함수
# from, import 뒤에 어떤 위치가 와도 가능

import pandas as pd
import numpy as np

# list -> dataframe
df = pd.DataFrame(data=[[2, 3, 4], [1, 2, 3]],
                  columns=['kor', 'math', 'eng'])
print(df.head())

# csv -> df; comma sepertated
# 만약 탭이 구분자면, sep='\t' 추가
# csv만이 아니라 다양한 자료 추출 가능
df = pd.read_csv('emp.csv')

# 한 컬럼만 조회; select empno from emp;
# print(df['empno'])
# print(df.empno)

# 여러 컬럼 조회; select empno, ename from emp;
# print(df[['empno', 'ename']])

# .iloc; idx location
# .loc;  cols name location; 정확하게 값을 줘야 함

# print(df.index)
# 한 컬럼을 인덱스로 빼왔음
df = df.set_index('empno')
# print(df.index)
# print(df.shape)
# print(df.info())

# print(df.loc[7369:7521, 'ename':'hiredate'])
# print(df.iloc[:3, :-1])

# select * from emp where empno = 7521;
# print(df.loc[7521])
# print(df.loc[7521:7566, :])
# print(df.iloc[[2, 3]])

# print(df.iloc[2:4, 0:2])
# print(df.iloc[[2, 3], [0, 1]])
# print(df.loc[7521:7566, 'ename':'job'])

# print(df.iloc[:3, 1:6])
# print(df.loc[7369:7521, 'job':'comm'])

# 조건 필터링
# select * from emp where deptno = 10;
# print(df[df['deptno'] == 10])

# select ename, sal, deptno from emp where dept = 10;
# 세 가지 방법; [cl][cond], [cond][cl], [cond, cl]
# print(df[df['deptno'] == 10][['ename', 'sal', 'deptno']]) # 권장
# print(df[['ename', 'sal', 'deptno']][df['deptno'] == 10])

# print(df.loc[ df['deptno'] == 10, 'sal':'deptno'])


# 정렬
# select * from emp order by ename desc;
# print(df.sort_values(by='ename', ascending=False))

# null 조회; isna(), isnull()
# select * from emp where comm is null;
# print(df[df.comm.isnull()][['job', 'ename']])
# print(df[~ df['comm'].isnull()][['job', 'ename']])
# print(df[df.comm.isnull() == False][['job', 'ename']])


# select ename, job from emp where deptno = 30 and job = 'SALESMAN';
a = df[(df.deptno == 30) & (df.job == 'SALESMAN')][['ename', 'job']]

# 쿼리문법, select 문법, 필터문법

# select * from emp group by deptno;
# 그룹화한 열만 조회 가능
# select job, deptno, count(1)
# from emp
# group by job, deptno
# having count(1) >= 2
# order by job, deptno

# oracle 그룹함수; count, max, min, avg, sum

# 그룹함수; sql, python 비교
# count() value_counts()
# avg() mean()
# max(), min(), sum() 동일

# select deptno, avg(sal) from emp group by deptno;
Aa = df.groupby(by='deptno')['sal'].mean()

# select deptno, min(sal), max(sal) from emp group by deptno;
a = df.groupby(by='deptno')
a = df.groupby(by='deptno')['sal'].agg([max, min])

a = df[df.deptno == 10].groupby(by='deptno')['sal'].agg([max, min])

a = df.set_index('empno')
a = df.set_index('empno', inplace=True)

a = df.reset_index(inplace=True)
a = df.reset_index()


b = '완료'
print(a, b)

