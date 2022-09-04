/* SQL함수, function */
/* 문자열 함수 */
SELECT customername AS aa
FROM customers;

SELECT ASCII(customername) AS a
FROM customers;

SELECT ASCII('A') FROM DUAL;
#아스키코드 문자열을 숫자열(아스키 코드값)로 바꿔줌

#CHAR_LENGTH - (" ")내에 있는 모든 데이터의 문자열길이를 나타냄

SELECT CHAR_LENGTH("SQL Tutorial") AS LengthOfString; 

#주어진 아스키코드값을 해당 문자열로 나타낸다.
#아스키코드 97에 해당하는 문자값 'a'로 반환

SELECT CHAR(97) FROM DUAL;

#CHARACTER_LENGTH  - CHAR_LENGTH와 동일기능

SELECT CHARACTER_LENGTH("SQL Tutorial") AS LengthOfString; 

#CONCAT - (" ")간의 문자열을 이어준다.

SELECT CONCAT("SQL ", "Tutorial ", "is ", "fun!") AS ConcatenatedString; 

#CONCAT_WS ("-"으로 경계를 구분하여 이어준다.

SELECT CONCAT_WS("-", "SQL", "Tutorial", "is", "fun!") AS ConcatenatedString; 

#FIELD - 맨 앞에오는 문자가 그 다음 문자열상 몇번째에 오는지

SELECT FIELD("q", "s", "q", "l"); 

#FIND_IN_SET - 첫 문자열이 다음 문자열 상 몇번째에 위치하는지

SELECT FIND_IN_SET("q", "s,q,l"); 

#FORMAT - 소수 N째 자리까지 나타내기

SELECT FORMAT(250500.5634, 2);

#INSERT - 1~9번째 에 있는 문자열을 뒤의 문자열로 대체하기

SELECT INSERT("W3Schools.com", 1, 9, "Example");  

# 3이란 문자열이 첫 문자열 상 몇번째에 위치하는지

SELECT INSTR("W3Schools.com", "3") AS MatchPosition; 

#소문자로 나타내기

SELECT LCASE("SQL Tutorial is FUN!");

#왼쪽에 있는 문자열을 순서대로 N까지 나타내기

SELECT LEFT("SQL Tutorial", 3) AS ExtractString;

#문자열의 길이를 나타내기

SELECT LENGTH("SQL Tutorial") AS LengthOfString; 

#3이란 문자열이 오른쪽 문자열 상 몇번째에 위치하는지

SELECT LOCATE("3", "W3Schools.com") AS MatchPosition; 

#lCASE 함수와 동일기능 - 소문자로 반환

SELECT LOWER("SQL Tutorial is FUN!");

#왼쪽에 특정문자를 원하는 자리수만큼 채워서 반환
사용법 : LPAD(원본문자열 , 원하는 자리수, 채울 문자열)
ex ) SELECT LPAD('ABC',10,'0')  FROM DUAL;
결과 : 0000000ABC

SELECT LPAD("SQL Tutorial", 20, "ABC");

#문자열 중 왼쪽 공백을 없앤다.

SELECT LTRIM("     SQL Tutorial") AS LeftTrimmedString;

#문자열 중 시작위치부터 개수만큼 출력 

SELECT MID("SQL Tutorial", 5, 3) AS ExtractString;

#함수만 해석한다면 위치를 반환하라 정도? 맞는말이다 
#위치를 반화하는것이다 하지만 비교하는 문자의 값이 
#비교할 데이터와 일치해야만 위치를 반환한다.

- select locate('ayoe','qqkyoeqq');
문자'a'이후의 값'yoe'는 일치하지만 첫문자'a'와'k'가 일치하지 않기 때문에 
결과값은 '0'이된다. 
- select locate('kyoe','qqkyoeqq');
위와 같이 sql문을 작성하면 반환되는 값은 3이 된다. 
'kyoe'라는문자가 'qqkyoeqq'에 속해있기때문에 그결과는 참이되고
 문자'kyoe'의 위치를 반환하게 되는것이다.


SELECT POSITION("3" IN "W3Schools.com") AS MatchPosition;