/*SQL함수,FUNCTION */
SELECT customername AS aa
FROM customers;

SELECT ascii(customername) AS aa
FROM customers;

SELECT ASCII('K');
SELECT CHAR_LENGTH("SQL Tutorial") AS LengthOfString;
SELECT CONCAT("SQL ", "Tutorial ", "is ", "fun!") AS ConcatenatedString;
SELECT CONCAT_WS("-", "SQL", "Tutorial", "is", "fun!") AS ConcatenatedString;
SELECT FIELD("q", "s", "q", "l");#같은 문자 갯수 찾기
SELECT FIELD("c", "a", "b");
SELECT FIND_IN_SET("q", "s,q,l");#q라는 문자가 다음 문자열에 몇번째에 있는지
SELECT FORMAT(250500.5634, 2);#숫자 천단위 앞에 컴마로 정형화
SELECT INSERT("W3Schools.com", 1, 9, "Example");
#1부터9번째 자리의 문자w3schools를 example로 바꿈
SELECT INSTR("W3Schools.com", "3") AS MatchPosition;
#3이 지칭하는 w3schools.com안의 3의 위치가 2번째라는 것을 알림..
SELECT INSTR("W3Schools.com", "COM") AS MatchPosition;
#com의 시작 문자열 위치는 11자리부터.
SELECT LCASE("SQL Tutorial is FUN!");
#lowcase의 약어 (소문자로 전환)
SELECT LEFT("SQL Tutorial", 3) AS ExtractString;
#왼쪽부터 3번째자리의 문자열만 보여줌.
SELECT LENGTH("SQL Tutorial") AS LengthOfString;
#문자열의 길이를 보여줌 스페이스포함.
SELECT LOCATE("3", "W3Schools.com") AS MatchPosition;
#위치를 문자열에 3이라는 숫자의 위치는 2번째라는 것을 보여줌.
SELECT LOWER("SQL Tutorial is FUN!");
#lcase와 같음.
SELECT LPAD("SQL Tutorial", 20, "ABC");
#문자열의 길이가 20이 될때까지 왼쪽에서부터 abc를 채워서 정렬
SELECT rPAD("SQL Tutorial", 20, "ABC");
#문자열의 길이가 20이 될때까지 오른쪽에서부터 abc를 채워서 정렬
SELECT LTRIM("     SQL Tutorial") AS LeftTrimmedString;
#문자열""안에 빈공간을 삭제해서 보여줌.
SELECT MID("SQL Tutorial", 5, 3) AS ExtractString;
#substr과 같은 함수로 5번째 문자열부터 8번째자리까지 보여줌.
SELECT POSITION("3" IN "W3Schools.com") AS MatchPosition;
#locate와 같음.
SELECT REPEAT("SQL Tutorial", 3);
#sql tutorial을 3번 반복.
SELECT REPLACE("SQL Tutorial", "SQL", "HTML");
#sql을 html로 재배치. 출력결과는 HTML Tutorial
SELECT REVERSE("SQL Tutorial");
#sql tutorial의 문자열을 역순으로 보여줌lairotuT LQS
SELECT RIGHT("SQL Tutorial is cool", 4) AS ExtractString;
#오른쪽부터 문자열을 샘. 출력결과는 cool
SELECT RTRIM("SQL Tutorial     ") AS RightTrimmedString;
#""문자열안의 우측 빈공간 제거
SELECT SPACE(10);
#스페이스 10개 띄운 효과. 디폴트값이 아님.
SELECT STRCMP("SQL Tutorial", "SQL Tutoial");
#문자열 2개의 차이점을 찾아서 수로 표현.
#substr,substring,mid 같은 표현.
SELECT SUBSTRING_INDEX("www.w3schools.com", ".", 1);
#.구분자를 둔 1번째 www
SELECT TRIM('    SQL Tutorial    ') AS TrimmedString;
#우측 좌측 빈공간 삭제.
SELECT UCASE("SQL Tutorial is FUN!");
#upper case의 약어(대문자로)
SELECT UPPER("SQL Tutorial is FUN!");
#ucase와 같음.
SELECT VERSION();
SELECT USER();
SELECT SYSTEM_USER();
SELECT SESSION_USER();
SELECT NULLIF(25, "world");
SELECT NULLIF("2017-09-25", "2017-08-25");
SELECT NULLIF("Hello", "world");