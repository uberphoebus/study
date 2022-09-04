from konlpy.tag import Okt
import re
okt = Okt()

# 정규 표현식을 통해 온점을 제거하는 정제 작업.
token = re.sub("\.","","정부가 발표하는 물가상승률과 소비자가 느끼는 물가상승률은 다르다.")

# OKT 형태소 분석기를 통해 토큰화 작업을 수행한 뒤에, token에다가 넣음.
token = okt.morphs(token)

word2index = {}
bow = []
for voca in token:




from sklearn.feature_extraction.text import CountVectorizer
corpus = ['you know I want your love. because I love you.']
vector = CountVectorizer()

# 코퍼스로부터 각 단어의 빈도수를 기록
print(vector.fit_transform(corpus).toarray())

# 각 단어의 인덱스가 어떻게 부여되었는지를 출력
print(vector.vocabulary_)
