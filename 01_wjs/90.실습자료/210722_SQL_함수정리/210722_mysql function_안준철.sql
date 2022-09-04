# SQL 함수
SELECT customername AS aa
  FROM customers;

SELECT ASCII(customername) AS aa
  FROM customers;
  
SELECT ASCII('A') FROM DUAL;
SELECT ASCII('A');

SELECT CONCAT("a", "s", "c", "i") AS aa;
SELECT*FROM customers;

SELECT CONCAT(customername, '-', contactname)
  FROM customers;

SELECT CONCAT_WS("-", "a", "s", "c", "i") AS aa;

SELECT FIELD("Q", "s", 'q', 'l'); #첫번째꺼가 뒤에 남은 문자중에 몇번째에 있는가 (2)
SELECT FIND_IN_SET('q','s,q,l'); #천번째 단어가 뒷 문자배열중 몇 번째에 있는가 (2)

SELECT FORMAT(12345.12345, 3); #뒤 숫자만큼만 소수점 아래 남기고 삭제 (12,345.123)

SELECT INSERT("naver.com", 1, 5, "zzzzzzzzz"); #첫 문자열의 a번째~b번째를 뒤의 문자열로 대체 (zzzzzzzzz.com) 

SELECT INSTR("naver.com", "v") AS pathway; #문자열에서 몇번째에 있는가 (3)

SELECT LCASE("My life is good!");  #전체를 소문자로 (my life is good!) 

SELECT LEFT("freestyle", 3) AS ExtractString; #왼쪽부터 n번째 숫자까지 (fre)

SELECT LENGTH("freestyle") AS LengthOfString; #글자수 (9)

SELECT locate("0", "32105601") AS MatchPosition; #글자가 몇번째에 있는가 (4) *여러개가 있을 경우 처음 발견위치만 나옴

SELECT LOWER("My life is Good!"); #Lcase와 동일

SELECT LPAD("Dirty cash", 20, "bzz"); #문자열 앞에 뒤의 문자열을 반복 추가해 길이를 맞춰줌 (bzzbzzbzzbDirty cash)

SELECT LTRIM("        dirty cash") AS LseftTrimmedString; #문자열의 빈공간 제거 (dirty cash)

SELECT MID("Dirty cash", 4, 2) AS ExtractString; #문자열의 a번쨰부터 b글자 (ty)

SELECT POSITION("1" IN "ASH 1sland") AS MatchPosition; #문자열에서 몇번째에 있는가 (5)

SELECT repeat('ok', 3); #문자열을 n번 반복 (okokok)

SELECT REPLACE("Dirty cash", "cash", "Gang!"); #문자열 대체 (Dirty Gang!)

SELECT REVERSE("dirty"); #문자열 뒤집기 (ytrid)

SELECT RIGHT("ASH Island", 3) AS ExtractString; #오른쪽에서부터 n번째 문자열 (and)

SELECT RPAD("ok", 20, "zzz"); #오른쪽에 문자열 반복추가하여 길이 맞춤(okzzzzzzzzzzzzzzzzzzz)

SELECT RTRIM("dirty cash             ") AS RightTrimmedString; #(dirty cash)

SELECT SPACE(5); #space키를 입력한 횟수만큼 입력 (     )

SELECT STRCMP("famous", "change"); #두 문자열을 비교, 같으면0  다르면1

SELECT SUBSTR("famous", 4, 2) AS ExtractString; #4번째부터 2글자 (ou)

SELECT SUBSTRING("ASH Island", 4, 4) AS ExtractString; #( Isl)

SELECT SUBSTRING_INDEX("www.naver.com", ".", 1); #찾으려는 1번째 .이 나오기 전까지의 문자열 (www)

SELECT TRIM('      famous  sdf   ') AS TrimmedString; #양쪽 여백 제거 (famous  sdf)

SELECT UCASE("famous"); #(FAMOUS)

SELECT UPPER('cash'); #(CASH)

SELECT ABS(-243.5); #절댓값 (243.5)

SELECT ACOS(0.25); #아크코사인
        SIN       #사인
       ASIN       #아크사인
		  TAN       #탄젠트
       ATAN       #아크탄젠트
SELECT ATAN2(0.50, 1);   #아크탄젠트
SELECT AVG(Price) AS AveragePrice FROM products #평균

SELECT CEIL(25.75) #가장 가까운 정수

SELECT CEILING(25.75); #가장 가까운 같거나 더 큰 정수

SELECT COS(2); #코사인
       COT     #코탄젠트
       
SELECT COUNT(ProductID) AS NumberOfProducts FROM products; #갯수 

SELECT DEGREES(1.5); #라디안값으로 변환

SELECT 10 DIV 5; #10/5

SELECT EXP(1); #e^n

SELECT FLOOR(25.75); #값보다 크지 않은 가장 가까운 정수 (25)

SELECT GREATEST(3, 12, 34, 8, 25); #문자열중 가장큰 수 (34)

SELECT LEAST(3, 12, 34, 8, 25); #가장 작은수 (3)

SELECT LN(2); #ln함수

SELECT LOG(2); #자연로그2

SELECT LOG10(2); #log2

       LOG2 #밑이 2
       
       MAX #가장 비싼거
       MIN #가장 싼거

 SELECT MOD(18, 4); #18/4 의 나머지
 
 SELECT PI(); #파이
 
 SELECT POW(4, 2); #4^2
 
 SELECT POWER(4, 2); #4^2
 
 SELECT RADIANS(180); #180라디안 = 1파이
 
SELECT RAND(); #무작위의 십진법 수

SELECT ROUND(135.375, 2); #소수점 2자리만 표시하되 3째에서 반올림?

SELECT SIGN(255.5); #양수 1, 0은 0, 음수는 -1

SELECT SQRT(64); #루트

SELECT SUM(Quantity) AS TotalItemsOrdered FROM OrderDetails; #OrderDetails에 있는 전체 수량의 합

SELECT TRUNCATE(135.375, 2); #소수점 두번째 자리까지 표시. 이하 버림
 
 
 







