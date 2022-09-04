/**********문자열 함수************/

/*LEFT(string, number_of_chars)  - x의  왼쪽에서 n개 추출*/
SELECT LEFT("SQL Tutorial", 3) AS ExtractString;

/* LENGTH(string)  -  문자길이 추출*/
SELECT LENGTH("SQL Tutorial") AS LengthOfString;

/*LOCATE(substring, string, start) -  문자열 내 위치 찾기*/
SELECT LOCATE("3", "W3Schools.com") AS MatchPosition;

/*LOWER(text) - 대문자를 소문자로 변환*/
SELECT LOWER("SQL Tutorial is fun!")

/*LPAD(string, length, lpad_string) */
SELECT LPAD("SQL Tutorial", 20, "ABC");

/*LTRIM(string) -  왼쪽 스페이스 공백 없애고 출력*/
SELECT LTRIM("     SQL Tutorial") AS LeftTrimmedString;

/*MID(string, start, length) - 문자열의 n번째부터 m개 추출*/
SELECT MID("SQL Tutorial", 5, 3) AS ExtractString;

/*POSITION(substring IN string)  - 문자열 내  a의 위치 찾기*/
SELECT POSITION("3" IN "W3Schools.com") AS MatchPosition;

/*REPEAT(string, number) - 문자열 n번 반복*/
SELECT REPEAT("SQL Tutorial", 3);

/*REPLACE(string, from_string, new_string) -  문자열 내 A를 B로 바꾸기*/
SELECT REPLACE("SQL Tutorial", "SQL", "HTML");

/* REVERSE(string) - 문자열 뒤집기*/
SELECT REVERSE("SQL Tutorial");

/*RIGHT(string, number_of_chars)  -  오른쪽 n개 추출*/
SELECT RIGHT("SQL Tutorial is cool", 4) AS ExtractString;

/* SPACE(number) - 스페이스 공백 n개 출력*/
select space(10);

/* STRCMP(string1, string2)  -  두 문자열 비교해서 같으면 0, 다르면 -1 출력*/
SELECT STRCMP("SQL Tutorial", "SQL Tutorial");

/* SUBSTR(string, start, length)  -  n번째부터 m개 문자 추출*/
SELECT SUBSTR("SQL Tutorial", 5, 3) AS ExtractString;

/* SUBSTRING(string, start, length)  -  n번째부터 m개 문자 추출*/
SELECT SUBSTRING("SQL Tutorial", 5, 3) AS ExtractString;

/*SUBSTRING_INDEX(string, delimiter, number) - 문자열 내 "."가 2째로 나오는 것의 앞 문자열 모두 추출*/
SELECT SUBSTRING_INDEX("www.w3schools.com", ".", 1);

/*TRIM(string) - 문자열 내 모든 공백 제거하여 추출*/
SELECT TRIM('    SQL Tutorial    ') AS TrimmedString;

/* UCASE(text)  -  소문자를 대문자로 변환*/
SELECT UCASE("SQL Tutorial is FUN!");

/* UPPER(text) - 소문자를 대문자로 변환*/
SELECT UPPER("SQL Tutorial is FUN!");



/**********숫자  함수************/

/*ABS  -  ABS(number)*/
SELECT ABS(-243.5);

/*ACOS*/
SELECT ACOS(0.25);

/*ASIN*/
SELECT ASIN(0.25);

/*ATAN  -  ATAN(number) or ATAN(a, b)*/
SELECT ATAN(2.5);

/*ATAN2  -  ATAN2(a, b)*/
SELECT ATAN2(0.50, 1);

/*AVG  -  AVG(expression)*/
SELECT AVG(Price) AS AveragePrice FROM Products;

/*CEIL*/
SELECT CEIL(25.75);

/*CEILING*/
SELECT CEILING(25.75);

/*COS*/
SELECT COS(2);

/*COT*/
SELECT COT(6);

/*COINT  -  COUNT(expression)*/
SELECT COUNT(ProductID) AS NumberOfProducts FROM Products;

/*DEGRESS*/
SELECT DEGREES(1.5);

/*DIV  -  x DIV y   10/5 */
SELECT 10 DIV 5;

/*EXP*/
SELECT EXP(1);

/*FLOOR*/
SELECT FLOOR(25.75);


/*GREATEST  - GREATEST(arg1, arg2...)*/
SELECT GREATEST(3, 12, 34, 8, 25);


/*LEAST  -  LEAST(arg1, arg2...)*/
SELECT LEAST(3, 12, 34, 8, 25);

/*lN*/
SELECT LN(2);

/*LOG*/
SELECT LOG(2);

/*LOG10*/
SELECT LOG10(2);

/*LOG2*/
SELECT LOG2(6);

/*MAX  -  MAX(expression)*/
SELECT MAX(Price) AS LargestPrice FROM Products;

/*MIN  -  MIN(expression)*/
SELECT MIN(Price) AS SmallestPrice FROM Products;

/*MOD - MOD(x, y) or  x % y   or  x MOD y*/
SELECT MOD(18, 4);

/*PI -  PI()*/
SELECT PI();

/*POW  -  POW(x, y)*/
SELECT POW(4, 2);

/*POWER  - POWER(x, y)*/
SELECT POWER(4, 2);

/*RADIANS*/
SELECT RADIANS(180);

/*RAND  -  RAND(seed)*/
SELECT RAND();

/*ROUND  -  ROUND(number, decimals)*/
SELECT ROUND(135.375, 2);

/*SIGN  */
SELECT SIGN(255.5);

/*SIN  */
SELECT SIN(2);

/*SQRT  */
SELECT SQRT(64);

/*SUM  -  SUM(expression)*/
SELECT SUM(Quantity) AS TotalItemsOrdered FROM OrderDetails;

/*TAN  - */
SELECT TAN(1.75);

/*TRUNCATE  -  TRUNCATE(number, decimals)*/
SELECT TRUNCATE(135.375, 2);

SELECT DATE_ADD("2021-07-22", INTERVAL 10 DAY);