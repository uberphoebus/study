#문자를 아스키 코드값으로 변환

SELECT ASCII(customername) AS numcodeoffirstchar
FROM customers;

#문자열 길이
SELECT CHAR_LENGTH("SQL Tutorial");
SELECT CHARACTER_LENGTH("SQL Tutorial");

#문자열 연결
SELECT CONCAT("SQL ", "Tutorial ", 'is ', 'fun!');

#(구분 값, 문자, 문자 ...)
SELECT CONCAT_WS('-', 'SQL', 'Tutorial', 'is', 'fun');

#첫번재 문자열의 위치
SELECT FIELD("q",'s','q','l');

#FIND_IN_SET(str, strlist)
SELECT FIND_IN_SET('q','s,q,l');

#FORMAT(숫자, 소수이하자리수)  '#,###,###.##'
SELECT FORMAT(270654.31564, 2);

#지정된 위치에 특정 문자 수만큼 문자열 삽입
SELECT INSERT('W3Schools.com', 1, 9, 'example');

#(string1, string2) string1에서 string2가 처음 나타나는 위치
SELECT INSTR('W3School.com', '3');

#소문자로 변환
SELECT LCASE("SQL Tutorial is FUN!");
SELECT LOWER("SQL Tutorial is FUN!");

#문자열에서 왼쪽부터 *개의 문자추출
SELECT LEFT('SQL Tutorial', 3);

#문자열 길이
SELECT LENGTH('SQL Tutorial');

#문자열에서 3의 위치 반환
SELECT LOCATE('3', 'W3Schools.com');

#(Str, Length, Lpad_Str) 
#Str을 Lpad_Str로 왼쪽부터 채우기 (길이제한 Length)
SELECT LPAD("SQL Tutorial", 20, "ABC");

#(Str, Length, Rpad_Str) 오른쪽부터 채우기
SELECT RPAD('SQL Tutorial', 20, 'ABC');

#공백제거
SELECT LTRIM("     SQL Tutorial");

#후행 공백제거
SELECT RTRIM("SQL Tutorial    ");

#(str, start, lenth) start에서 시작하여 lenth만큼 추출
SELECT MID('SQL Tutorial', 5, 3);
SELECT SUBSTR('SQL Tutorial', 5, 3);
SELECT SUBSTRING('SQL Tutorial', 5, 3);

#('substr' in 'str') str에서 substr 검색 후 위치반환
SELECT POSITION('3' IN 'W3Schools.com');

#문자열 반복
SELECT repeat('SQL Tutorial', 3);

#(str, from_str, new_str) from을 new로 문자열 교체
SELECT REPLACE('SQL Tutorial', 'SQL', 'HTML');

#문자열 반전
SELECT REVERSE('SQL Tutorial');

#문자열에서 오른쪽부터 *개의 문자추출
SELECT RIGHT('SQL Tutorial is cool', 4);

#공백문자로 구성된 문자열 반환
SELECT SPACE(10);

/* 문자열 비교
 str1 = str2면 0반환,
 str1 < str2면 -1,
 str1 > str2면 1 */
SELECT STRCMP('SQL Tutorial', 'SQL Tutorial');

#구분 기호 하위 문자열 반환
SELECT SUBSTRING_INDEX('www.s3schools.com', '.', 1);
