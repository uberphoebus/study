import re

# abcd, book, desk
# ca?e : care, cafe, case, cave

p = re.compile('ca.e')
# . (ca.e): 하나의 문자를 의미 > care, cafe | caffe (X)
# ^ (^de) : 문자열의 시작 > desk, dest | fade (X)
# $ (se$) : 문자열의 끝 > case, base | face (X)

def print_match(m):
    if m:
        print(f'm.group() : {m.group()}') # 일치 문자열 반환
        print(f'm.string() : {m.string}') # 입력받은 문자열 반환
        print(f'm.start() : {m.start()}') # 일치하는 문자열 시작 인덱스
        print(f'm.end() : {m.end()}') # 일치하는 문자열 끝 인덱스
        print(f'm.span() : {m.span()}') # 일치하는 문자열의 시작 & 끝 인덱스
    else:
        print('매치 오류')

m = p.match('case')
print_match(m)

m = p.match('good case')
print_match(m)

m = p.match('careless') # 처음부터 일치하는지 확인
print_match(m)

m = p.search('good care') # 주어진 문자열 중 일치하는 것이 있는지 확인
print_match(m)

lst = p.findall('careless') # 일치하는 모든 것을 리스트로 반환
print(lst)

lst = p.findall('good care cafe')
print(lst)

# 1. p = re.compile('원하는 형태')
# 2. m = p.match() : 처음부터
# 3. m = p.search() : 문자열 중
# 4. lst = p.findall() : 모든 일치