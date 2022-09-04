
# import -------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn

from sklearn.model_selection import train_test_split # def
from sklearn.tree import DecisionTreeClassifier      # class
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score           # def

import warnings
warnings.filterwarnings(action='ignore')

# def, args, papram --------------------------------
# casting ; 형 변환, int(), str(), df.astype('int32')
# arg, param ; input
# def return ; type tuple
# *args      ; 여러 input, type tuple
# **kargs    ; keyword args, type dict, return dict
# key=param  ; param default value
# key=None   ; unnecessary param

def func1(in1, in2):      # in = parameter or argument
    print('func1 call')
    add = in1 + in2
    return in1, in2, add  # 호출했을 때 반환되는 부분(tuple)
def func2(str, *args):         # *는 여러 값, tuple로 입력
    print('func2 call', str)   # *args 는 맨뒤에만, 여러번 불가
    sum = args[0] + args[1] + args[2]
    return sum
def func3(str, **kwargs):  # keyword args, dict형태로 받음
    print(kwargs.items())  # k:v
    print(kwargs.keys())   # k
    print(kwargs.values()) # v
    print('func3 call')
    sum = kwargs[0] + kwargs[1] + kwargs[2]
    return kwargs          # dict, func3(id='kim', pw=11)
def func4(str, *args, **kwargs):
    print(str)
    print(args)    # tuple
    print(kwargs)  # dict
    return str
def func5(id, pw=0000, gen=1):   # key= ; param default value
    print(id, pw, gen)           # 기본값이 없다면, arg 반드시 입력
    return 'ok'                  # 기본값으로 전역변수도 가능
def func6(id=None):   # default 없이, 값이 올수도 안올수도 있을 때
    print(id)
    return 'ok'
def func7(id=None, pw='1111', gen=1, addr=None):
    print(id, pw, gen, addr)   # param을 주지 않아도 순서대로 인식
    return 'ok'                # 특정 param이라면 key= 지정

# class --------------------------------------------
class MyClass():
    point = 1000
    def clsFunc1(self, num):   # self 반드시 입력, self는 주소를 만들어서 받아주는 부분
        print('clsFunc1 call')
        print(point)
        self.num = num    # class 내부에 변수 저장
        return
    def clsFunc2():
        print('clsFunc2 call')
        print(point)

# self     ; class의 메모리 주소
# __init__ ; 생성자, class 호출마다 자동 실행
# method   ; class 내 함수
# function ; class 밖 함수

# class.__dict__
# self.__dict__
# dir(self)
# self.__dir__

# pakage, module, method, function -----------------
# pakage > module > [class] > [method] or function
# pakage     ; lib = API
# module     ; code file, *.py
# Attributes ; 속성 == 변수

# sklearn API example ------------------------------

# 1. DecisionTreeClassifier
# criterion="gini",
# splitter="best",     # 오버피팅일 때 랜덤 설정
# max_depth=None,      # 가지치는 깊이
# min_samples_split=2,
# min_samples_leaf=1,  # 바닥의 최소 샘플 개수
# max_features=None,   # 피쳐 개수
# random_state=None,   # seed

# 2. RandomForestClassifier
# n_estimators = 100, *, # tree
# criterion="gini",
# bootstrap=True,        # 복원추출, 추출 후 원본에서 다시 추출
# oob_score=False,       # 한번도 뽑히지 못한 tree, True하면 자체적으로 검증
# n_jobs=None,           # 가용 자원 설정
# random_state=None,     # seed
# verbose=0,             # 로그 메시지

# 3. train_test_split
# *arrays,           # 여러 개의 array
# test_size=None,
# train_size=None,
# random_state=None, # seed
# shuffle=True,      # 섞음
# stratify=None      # shape 개수만큼 입력