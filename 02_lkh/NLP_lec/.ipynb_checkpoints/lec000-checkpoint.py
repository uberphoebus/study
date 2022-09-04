# """한글, 숫자, 영어 빼고 전부 제거"""
def sub_special(s):
  return re.sub(r'[^ㄱ-ㅎㅏ-ㅣ가-힣0-9a-zA-Z ]','',s)

STOP_WORDS = ['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다']

def morph_and_stopword(s):
  token_ls = []
  #형태소 분석
  tmp = okt.morphs(s, stem=True)

  #불용어 처리
  for token in tmp:
    if token not in STOP_WORDS:
      token_ls.append(token)


# """TF-IDF로 만들기"""
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(df.content)
# 줄거리에 대해서 tf-idf 수행
print(tfidf_matrix.shape)  # (50000, 91575) = (rows, unique-words)


# 0.0, 0.0, 0.0, 0.12816105088299284 --> , 분자(내적계산) 시 0이 곱해져 유사도 스코어도 낮아짐
# 차원의 저주(Curse of dimensionality): 데이터차원 > 학습데이터차원 --> 알고리즘 성능 저하되는 현상
# 수많은 유니크 단어로 인한 차원 확대의 문제로, 특정 문서가 가지고 있지 않은 단어들 까지 모두 벡터화해서 생긴 문제
print(list(tfidf_matrix.toarray()[0]))



from konlpy.tag import Komoran
komoran = Komoran()
print(komoran.nouns("파이썬 자연어처리 프로젝트"))

count_vec = CountVectorizer(tokenizer=komoran.nouns)

doc = ["폴 크루그먼 뉴욕시립대학교 교수가 경기 부진을 극복하기 위해 과감한 재정 투입 조치를 취해야 한다고 제언했다."]
count_vec.fit(doc)
print(count_vec.vocabulary_)
-
{'폴 크루그먼': 11, '뉴욕': 3, '시립': 6, '대학교': 4, '교수': 1, '경기': 0, '부진': 5, '극복': 2, '재정': 7, '투입': 10, '조치': 9, '제언': 8}



"""코사인 유사도 구하기"""
from sklearn.metrics.pairwise import linear_kernel      #(50000, 50000)
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)  #array([[1., 0.01729075,  ..., 0.02042815],  [0.01729075, 1. , ..., 0]]

"""인덱스 테이블 만들기"""
indices = pd.Series(df.index, index=df.title).drop_duplicates()
print(indices)
# title
# 신림동드림                  0
# 머나먼 베트남                1
# 스탈린의 신부                2


"""추천 해주기"""


def movie_REC(title, cosine_sim=cosine_sim):
  idx = indices[title]
  sim_scores = list(enumerate(cosine_sim[idx]))  # 모든 영화와의 유사도 구하기
  sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True) # 유사도에 따라 영화들을 정렬
  sim_scores = sim_scores[1:11]   # 가장 유사한 10개의 영화를 받아옴
  movie_idx = [i[0] for i in sim_scores]  # 가장 유사한 10개 영화의 인덱스 받아옴

  # 기존에 읽어들인 데이터에서 해당 인덱스의 값들을 가져온다.
  result_df = df.iloc[movie_idx].copy()
  #스코어 컬럼 : 코사인 유사도 확인
  result_df['score'] = [i[1] for i in sim_scores]
  del result_df['content']
  # 가장 유사한 10개의 영화의 제목을 리턴
  return result_df

movie_REC("극장판 포켓몬스터 모두의 이야기")
