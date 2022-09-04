/*String Functions*/

# 대문자를 소문자로 변환
SELECT LCASE("SQL Tutorial IS fun!");

# left(x,3): x의  왼쪽 3개 읽기
SELECT LEFT ("SQL Tutorial",3) AS '왼쪽 세개 추출'

# 문자길이 추출
SELECT LENGTH("SQL Tutorial") AS 길이

# 문자열 내 위치 찾기
SELECT LOCATE("3", "W3schools.com") AS 위치

# 대문자를 소문자로 변환
SELECT LOWER("SQL Tutorial is fun!")

# # "나는배고프다"의 왼쪽에 "ABC"를 포함하여 길이 20의 문자열
SELECT LPAD("나는배고프다", 20, "ABC");

# 왼쪽 스페이스 공백 없애고 출력
SELECT LTRIM("     나는배고파");

# MID("문자열",n,m) : 문자열의 n번째부터 m개 추출
SELECT MID("SQL Tutorial",5,3) AS 뇸뇸;

# position("a" in "문자열") : 문자열 내  a의 위치 찾기
SELECT POSITION("3" IN "W3schools.`com") AS 뇸뇸;

# 문자열 n번 반복
SELECT REPEAT("배고파", 3);

# 문자열 내 A를 B로 바꾸기
SELECT REPLACE("배고프다","배","사과")

# 문자열 뒤집기
SELECT REVERSE("배고프다")

# 오른쪽 n개 추출
SELECT RIGHT("나는배가고프다",4)

# "나는배고프다"의 오른쪽에 "ABC"를 포함하여 길이 20의 문자열
SELECT RPAD("나는배고프다",20,"ABC");

# 오른쪽 스페이스 공백 없애고 출력
SELECT RTRIM("나는배고파    ");

# 스페이스 공백 n개 출력
select space(10);

# 두 문자열 비교해서 같으면 0, 다르면 -1 출력
SELECT STRCMP("나는 배고파", "나는 배고파")

# n번째부터 m개 문자 추출
SELECT SUBSTR("나와너는배고파요", 4, 3)

# n번째부터 m개 문자 추출
SELECT SUBSTRING("나와너는배고파요",4,3)

# 문자열 내 "."가 2째로 나오는 것의 앞 문자열 모두 추출
SELECT SUBSTRING_INDEX("안녕.잘가.잘있어",".",2);

# 문자열 내 모든 공백 제거하여 추출
SELECT TRIM('    나는배고파    ')

# 소문자를 대문자로 변환
SELECT UCASE("I'm so happy!");

# 소문자를 대문자로 변환
SELECT UPPER("I'm so happy!");

/*Numeric Function*/

# 절대값
SELECT ABS(-243.5);



/*Numeric Function*/

# 날짜  더하기
SELECT ADDDATE("2021-07-22", INTERVAL 10 DAY);
SELECT ADDDATE("2021-07-22 09:34:21", INTERVAL 15 MINUTE);

# 초단위 시간 더하기
SELECT ADDTIME("2021-07-2 09:34:21", "2");

# 현재 날짜 추출
SELECT CURDATE();
SELECT CURRENT_DATE();

# 현재 시간 추출
SELECT CURRENT_TIME();
SELECT CURTIME();

# 현재 날짜와 시간 추출
SELECT CURRENT_TIMESTAMP();

# 날짜 추출
SELECT DATE("2021-07-22");

# 날짜 간 일 수 차이 : 나중 날짜, 시작 날짜
SELECT DATEDIFF("2021-07-25", "2021-07-22");

# 날짜 더하기
SELECT DATE_ADD("2021-07-22", INTERVAL 10 DAY);

# format 함수: 날짜를 연도 형태로 변환 출력
SELECT DATE_FORMAT("2017-06-15", "%Y");