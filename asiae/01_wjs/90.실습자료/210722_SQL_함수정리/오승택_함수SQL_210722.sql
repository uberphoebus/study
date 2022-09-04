#### 함수 총정리 ####

#ASCII
SELECT(customername) numcodeoffirstchar
 FROM customers;
 
#char_length
SELECT CHAR_LENGTH(customername) 이름길이
 FROM customers;
 
#character_length
SELECT CHARACTER_LENGTH(customername) 이름길이
 FROM customers;
 
#concat
SELECT CONCAT(address,'',postalcode,'',city) 주소
 FROM customers;
 
#concat_ws
SELECT CONCAT_WS('',address,postalcode,city) 주소
 FROM customers;
 
#field
SELECT FIELD('q','b','c');

#find in set
SELECT FIND_IN_SET('a','s,q,l');

#format 지정한소숫점다음자리에서 반올림
SELECT FORMAT(2503040.39449, 2);
SELECT FORMAT(2503040.39449, 4);

#insert 지정한 범위내 글자삽입
SELECT INSERT('w3schoools.com', 1, 9, 'hello');
SELECT INSERT('w3schoools.com', 1, 3, 'hello');

#instr
SELECT INSTR('W3Schools.com', 'com') 동일;
SELECT INSTR('W3Schools.com', 'w3s') 동일;

SELECT INSTR(customername, 'k')
 FROM customers;
 
#lcase 소문자로 바꾸기
SELECT LCASE(CustomerName)  LowercaseCustomerName
FROM Customers;
 
#left
SELECT LEFT(CustomerName, 5) as 5자리
FROM customers;


SELECT LEFT(CustomerName, 2) AS 2자리
FROM customers;


#length 길이파악
SELECT LENGTH(CustomerName) 이름길이
FROM Customers;


#locate 위치파악
SELECT LOCATE('b', customername)
 FROM customers;
 

SELECT LOCATE('a', customername)
 FROM customers;
 
SELECT customername
 FROM customers; #확인
 
#lower 
SELECT LOWER(CustomerName)
FROM customers;

#lpad 지정한 숫자까지 지정문자로 채운다
SELECT LPAD(CustomerName, 30, "C") LeftPadCustomerName
FROM Customers;

#mid
SELECT MID(CustomerName, 2, 5) 추출값
FROM customers;

#position
SELECT POSITION("3" IN "W3Schools.com") 위치;
SELECT POSITION('o' IN "W3Schools.com") 위치; # 문자가 많을땐 그걸 각각 나타내주진않는거같음

#repeat 반복
SELECT REPEAT(CustomerName, 2)
FROM customers;

#replace 단어를 바꾸기
SELECT REPLACE("SQL Tutorial", "SQL", "HTML");
SELECT REPLACE("강동구 둔촌동", "강동구", "234");

#reverse 역순배열
SELECT REVERSE("SQL Tutorial");


#right 오른쪽서부터 지정숫자까지 추출
SELECT RIGHT(CustomerName, 5) AS ExtractString
FROM customers;

SELECT RIGHT(CustomerName, 10) AS ExtractString
FROM customers;

#rpad 지정된숫자만큼 오른쪽에 채운다
SELECT RPAD(customername, 40, 'k')
FROM customers;

#rtrim 
SELECT RTRIM("SQL Tutorial     ")  RightTrimmedString;

#space
SELECT SPACE(3);

#
SELECT STRCMP("SQL Tutorial", "HTML Tutorial");

#substring  지정숫자까지 추출
SELECT SUBSTRING(CustomerName, 2, 5) AS ExtractString
FROM customers;

#substring_index  = 구분문자 갯수나오기전까지 출력
SELECT SUBSTRING_INDEX("www.w3schools.com", ".", 2);
SELECT SUBSTRING_INDEX("www.w3schools.com", ".", 1);

#trim 좌우 스페이스를 없애준다
SELECT TRIM('    SQL Tutorial    ') AS TrimmedString;
SELECT TRIM('           jdfkjej   ') AS 공백제거

#upcase 대문자변환
SELECT UCASE(Customername) 대문자변환
 FROM customers;
 
#uppercase
SELECT UPPER(CustomerName) AS UppercaseCustomerName
FROM Customers;