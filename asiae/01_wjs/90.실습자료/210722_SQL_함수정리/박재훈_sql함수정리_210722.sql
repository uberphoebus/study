/* sql 함수 */

/* 문자열 */

# 첫 문자열의 아스키코드
SELECT ascii(customername) AS a FROM customers;

# 문자열 길이
SELECT CHAR_LENGTH('sql tut');

SELECT customername, CHAR_LENGTH(customername)
	FROM customers
	WHERE CHAR_LENGTH(customername) > 30;

# 문자열 조합
SELECT CONCAT(customername, '-', contactname)
	FROM customers;

CONCAT_WS

# 문자열의 자리 조회(대소 구분 없음)
SELECT FIELD('q', 's', 'q', 'l');

# 전체 문자열에서 조회
FIND_IN_SET

# 포맷; 자주 사용. 표현 틀
SELECT FORMAT(250500.312123, 2);

# 처음 나타나는 문자 위치
SELECT INSTR('abcd', 'c');

# 소문자화 (lower 동일)
SELECT LCASE('ABCD');

# 좌측으로부터 n개 문자열 추출
SELECT LEFT('abcdefg', 4);
-- right는 우측으로부터

# 문자열 길이
SELECT LENGTH('abcde');

# 문자 위치 검색(position 동일)
SELECT LOCATE('d', 'abcde', 3);
-- n은 시작 위치

# 자릿수만큼 좌측부터  특정 문자열 채움
SELECT LPAD('12345', 20, 'abc');
-- rpad는 우측부터 채움

# 좌측 빈칸 제거
SELECT LTRIM('     abc');
-- rtrim 우측 빈칸 제거

# 문자열 추출, a부터 b개
SELECT MID('abcdefg', 3, 3);
-- substr, substring 동일


# 문자열 n번 반복
SELECT repeat('abc', 4);

# 문자열 수정, a를 b로
SELECT REPLACE('abc123', '123', 'def');

# 역순 정렬
SELECT REVERSE('abcde');

# 빈칸 생성
SELECT SPACE(5);

# 문자열 길이 비교
SELECT STRCMP('abc', 'ab');
-- 길이가 같으면 0
-- 앞 문자열이 짧으면 -1
-- 앞 문자열이 길면 1

# 특정 문자열 n번 반복 이전 문자열 출력
SELECT SUBSTRING_INDEX('abcdabcdabcd', 'b', 2);

# 앞 뒤의 빈칸 제거
SELECT TRIM('     abcd     ');

# 대문자화(upper 동일)
SELECT UCASE('abcd');


/* 숫자 */

# 절대값
SELECT ABS(-123.4);

# arc 코사인(cos)
SELECT ACOS(0.123);

# acr 사인(sin)
SELECT ASIN(0.123);

# arc 탄젠트(cot, tan)
SELECT ATAN(1.23);

# arc 탄젠트
SELECT ATAN2(1.23, 0.123);

# 평균
SELECT AVG();

# 특정 수 이상의 최소 정수(ceiling 동일)
SELECT CEIL(123);
-- floor는 이하

# 갯수 셈
SELECT COUNT();

# 라디안 값 변환
SELECT DEGREES(3.5);

# 나누기 몫
SELECT 20 DIV 3;

# e
SELECT EXP(1);

# 숫자 목록의 최대값
SELECT GREATEST(4, 1, 5, 231, 50);
-- least 최솟값

# 자연로그
SELECT LN(10);

# 로그(log10, log2)
SELECT LOG(2, 8);

# 최대값, 최솟값
SELECT MAX();
SELECT MIN();

# 나눈 나머지
SELECT MOD(20, 3);
SELECT 20 MOD 3;
SELECT 20 % 3;

# PI ?
SELECT PI();

# 제곱(power 동일)
SELECT POW(2, 10);

# 라디안으로
SELECT RADIANS(360);

# 0 이상 1미만의 무작위 수
SELECT RAND();

# 특정 소수점 자릿수까지 출력
SELECT ROUND(123.4567, 3);

# 부호
SELECT SIGN(-123);
-- 양수 1, 0 0, 음수 -1

# 제곱근
SELECT SQRT(100);

# 합계
SELECT SUM();

# n번째 소수점까지 표시
SELECT TRUNCATE(123.4567, 3);


##################################################



