'''

<OracleDB>

- pk; 고유키. 테이블당 하나지만, pk를 구성하는 컬럼은 여러 개 가능
      deptno number(2) constraint pk_dept primary key, 별칭 부여
- fk; 다른 pk를 가져다 쓴 컬럼

- date; 날짜 연산시 반드시 사용
- number(a, b); 소숫점 포함 총 a자리, 소숫점 b자리

- ERD; 개체-관계. tb의 cols, pk, fk의 관계도

- oracle은 대소문자 구분하지 않으나, 대부분 db는 구분
- oracle은 문자열에 ''만 사용 가능, "" 사용 불가
- 다만 숫자는 '' 상관 없이 숫자로 인식

- 현업에서 * 사용 지양, 서버에 부하

- CRUD

1. insert

insert into tb [(cols, ...)]
values (vls, ...)

- 컬럼의 순서/개수와 val의 순서/개수 동일해야 함

- null; unknown value. 조건문에서 조회되지 않음
        where a is null / is not null
        null과 연산 주의. 모든 결과값 null.

- DB 확인사항; 컬럼의 pk와 null
- rows, cols = a, b ; a개 레코드, b개 컬럼

- commit; db 적용
- rollbakc; 연산과정 롤백, commit 이후에는 불가

2. update; 반드시 원본데이터와 조건문 확인

update tb
set col1 = vl1, col2 = vl2, ...
where cond;

3. delete; 데이터만 삭제, 마찬가지로 확인
delete
from tb

4. drop; 테이블 삭제
- fk가 존재한다면 삭제 불가능

 drop table tb cascade;
 - fk 연관 테이블까지 삭제


- JOIN; from 뒤 tb이 여러개인 경우
- 반드시 cols가 어느 tb 것인지 지정, 원본 권장
- 꼬챙이에 한줄로 엮는 개념
- 기준 테이블은 레코드의 개수가 아니라,
  group by의 개수가 많은 테이블

1. self join
- 한 테이블에 직원번호와 사수번호가 있을 경우
- 사수번호를 다시 직원번호에서 찾음

2. inner join
- default join

3. outer join
- 기준 테이블(게시글)과 다른 테이블(댓글) 관계
- 게시글은 댓글이 없어도 표시가 되어야 하지만,
  댓글은 반드시 게시글에 종속되어 있음.

- orcale 문법; (+)
select *
from emp e, dept d
where e.deptno(+) = d.deptno;

- ANSI 문법; [right/left] outer join on
select *
from emp e, dept d right outer join on e.deptno = d.deptno;


- SUB Query; select, from, where 등에 들어간 쿼리
- Inline View; from절 내의 서브쿼리
- 어느 위치든 사용 가능

- from dual; 결과물을 한 줄만 조회


- ERD 생성; sqldev - 파일 - Data Modeler - 임포트 - 데이터 딕셔너리
1. DB 접속
2. DB 선택; AI
3. 객체 선택; 테이블 선택
4. 모델 비교 - 병합


- tb 내보내기;
1. 테이블 우클릭 - 익스포트
2. sql 사용한다면 ddl, 형식 insert 혹은 다른 형식 선택
3. 한글이 있다면 인코딩 utf-8, 영어만이라면 MS949


- tb 가져오기;
1. 테이블 폴더 우클릭 - 데이터 임포트
2. 열 정의시, 데이터 확인하고 크기/자릿수 넉넉하게
'''

"""

--join
select *
from emp e, dept d
where e.deptno = d.deptno;

select *
from emp e join dept d on e.deptno = d.deptno;

select *
from emp e inner join dept d on e.deptno = d.deptno;


--self join
select *
from emp e, emp e1
where e.mgr = e1.empno;

select *
from emp e join emp e1 on e.mgr = e1.empno;

--outer join
select *
from emp e, dept d
where e.deptno(+) = d.deptno;

select *
from emp e right outer join dept d on e.deptno = d.deptno;

select *
from dept d left outer join emp e on e.deptno = d.deptno;

-- cadinality join
select *
from emp, dept;

-- 급여 1000 이상
select *
from emp
where sal >= 1000;

-- 급여 3000 이상인 사원의 직업과 같은 직업 사람들
select *
from emp
where job in (select distinct job from emp where sal >= 3000);

--select의 서브쿼리
select distinct deptno, count(deptno) cnt
from emp
group by deptno;

select (select count(1) from emp where deptno = 10) as dept10,
       (select count(1) from emp where deptno = 20) as dept20
from dual;
--from emp limit 1;


-- 1. 회원별 주문 상품 통계
-- 회원아이디 상품번호 상품개수 구매금액
-- users.user_id, goods.good_seq, orders_goods.order_amount, order_goods.order_price
-- (조건; 주문건이 없더라도 회원 출력)

select u.user_id, og.good_seq, og.order_amount, og.order_price
from users u, orders o, orders_goods og
where u.user_seq = o.user_seq(+)
      and o.order_code = og.order_code(+);

-- 2. 업체별 공급 상품 리스트
-- 업체번호 업체명 상품번호 상품명
-- com_seq, com_name, good_seq, good_name
-- (조건; 상품이 없더라도 업체명 출력)

select c.com_seq, c.com_name, cg.good_seq, g.good_name
from company c, company_goods cg, goods g
where c.com_seq = cg.com_seq(+)
      and cg.good_seq = g.good_seq(+);

-- 1번 문제 예시 답안
select u.user_id, og.good_seq, og.order_amount, og.order_price
from users u, orders o, orders_goods og
where u.user_seq = o.user_seq(+)
      and o.order_code = og.order_code(+);

-- 2번 문제 예시 답안
select c.com_seq, c.com_name, g.good_seq, g.good_name
from company c, company_goods cg, goods g
where c.com_seq = cg.com_seq(+)
      and g.good_seq(+) = cg.good_seq;

--이정도면 현장 직무에서 가능

--남성 여성 비율
select sex, count(1)
from titanic
group by sex;

-- join : from 절에 무조건 테이블이 2개 이상이면 된다.
--        14rows * 4rows : 카디널리티곱
select *
from emp , dept;


-- (self) 조인 Orale문법
select *
from emp e, emp e1
where e.mgr = e1.empno;
-- (self) 조인 Orale문법
select *
from emp e join emp e1
on e.mgr = e1.empno;


-- (inner) 조인 Orale문법
select *
from emp e, dept d
where e.deptno = d.deptno;

-- (inner) 조인 ANSI-SQL
select *
from emp e inner join dept d
--from emp e join dept d
on e.deptno = d.deptno;

-----------기준잡는방법 : 레코트갯수X, 경우의수(종류) 다 갖고있는 테이블이 기준 
select distinct deptno
from dept;

select deptno
from emp
group by deptno;


-- (outer) 조인 Orale문법
select e.ename, e.empno, e.deptno, d.deptno, d.dname
from dept d, emp e 
where e.deptno(+) = d.deptno;
-- (right outer) 조인 ANSI-SQL
select *
from emp e right outer join dept d
on e.deptno = d.deptno;
-- (left outer) 조인 ANSI-SQL
select *
from  dept d left outer join emp e on e.deptno = d.deptno
where e.deptno= 10;



"""


# pip install cx-Oracle
# cx_Oracle 패키지 모듈들을 import
import cx_Oracle as oci

# Oracle 서버와 연결(Connection 맺기)
conn = oci.connect('ai/0000@localhost:1521/xe')

# Connection 확인
print(conn.version)

# Oracle DB의 test_member 테이블 검색(select)
cursor = conn.cursor() # cursor 객체 얻어오기
cursor.execute('select * from titanic') # SQL 문장 실행
# print(cursor.fetchall())
# for rs in cursor:
#     print(rs)

cursor.close() # cursor 객체 닫기

# Oracle 서버와 연결 끊기
conn.close()

# conn과 close를 반복문 밖에 둬야 함
# conn.close()는 항상 해야 함
# with ~ conn. 자동으로 닫아주는 기능.

# 읽은 데이터를 df화
# [1 2 3] array 타입
# array 안의 array ; matrix(행렬)
#  [], (), {}
# 리스트, 튜플, 딕셔너리, 어레이 모두 df화 가능

import pandas as pd

list = [(1, 0, 'C'), (2, 1, 'C')]
tdf = pd.DataFrame(data=list, columns=['pno', 'sb', 'em'])
print(tdf.head())

df = pd.read_csv('titanic_sample.csv')
print(df.head())