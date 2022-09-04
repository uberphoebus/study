/*sql함수 , funtion */


##ascii 코드 리턴
SELECT customername AS aa
  FROM customers;
  
SELECT ascii(customername) AS aa
  FROM customers;
  
SELECT ASCII('A') FROM DUAL;


##문자 길이수 반환
SELECT CHAR_LENGTH("sql tutorial") 
    AS LENGTHOFstring;
    
    
##문자수 번환 
SELECT CHARACTER_LENGTH(CustomerName) 
    AS LengthOfName
    FROM Customers;


##문자 합치기    
SELECT CONCAT(address," ",postalcode," ",city) AS address
  FROM customers;

##문자 합치기 
SELECT CONCAT_WS(" ",address, postalcode, city) AS address
  FROM customers;
  
##리스트의 첫번째 값이  몇번째에 있는지 반환
SELECT FIELD(5,0,102,3,4,5);

##찾고자 하는 값이 리스트의 몇번째에 있는지를 반환
SELECT FIND_IN_SET("q","s,q,l");

##0번째 자리에서 반올림
SELECT FORMAT(250500.5634,1);

##1번째 부터 9개 글자를 원하는 문자 대신 삽입
SELECT INSERT("W3Schools.com", 1, 9, "Example");

##찾고자 하는 문자열 위치 찾기
SELECT INSTR("W3Schools.com", "3") 
    AS MatchPosition;
    

##대문자 소문자로 변환
SELECT LCASE(CustomerName) 
AS LowercaseCustomerName
FROM Customers;

##왼쪽에서 5개 추출
SELECT LEFT(CustomerName, 5) 
AS ExtractString
FROM Customers;

##문자열 길이
SELECT LENGTH("SQL Tutorial") 
    AS LengthOfString;
    
    
##찾고자 하는 문자열 위치 반환
SELECT LOCATE("3", "W3Schools.com") 
    AS MatchPosition;

##소문자로
SELECT LOWER("SQL Tutorial is FUN!");


##글자수 맞추기 위해 원하는 문자로 왼쪽에서부터 글자수 채움
SELECT LPAD(CustomerName, 30, "ABC") 
    AS LeftPadCustomerName
  FROM Customers;
  
  
##왼쪽 빈공간 제거
SELECT LTRIM("     SQL Tutorial") 
          AS LeftTrimmedString;
          
##왼쪽에서 부터 원하는 갯수만큼 글자 추출 공백포함
SELECT MID("SQL Tutorial", 5, 3) 
        AS ExtractString;
        
        
 ##찾는 글자의 위치값 반환       
SELECT position("3" IN "W3Schools.com") 
    AS MatchPsition;
    

##입력 횟수만큼 문자 반복
SELECT repeat("sql tutorial",3);


##원하는 문자를 원하는 문자로 변환
SELECT REPLACE("sql tutorial","sql","html");

##글자를 거꾸로 뒤집기
SELECT REVERSE("SQL Tutorial");

##오른쪽에서부터 컷
SELECT RIGHT("sql tutorial is cool",4) 
    AS extractstring;
    
    
##오른쪽에서부터 원하는 수만큼 문자 반복 
SELECT RPAD("sql tutorial",20,"abc");

##왼쪽 공백 제거
SELECT RTRIM("sql tutorial    ") 
    AS RigthTrimmesString;
    
##문자 반환
SELECT SPACE(20);

##두 문자수를 비교 같으면 0
SELECT STRCMP("sql tutorial","sql tutorial");


##원하는 위치의 갯수만큼 컷해서 반환
SELECT SUBSTR("SQL Tutorial", 5, 3)
    AS ExtractString;

SELECT SUBSTRING("SQL Tutorial", 5, 3) 
    AS ExtractString;

##"."으로 나눠지는 것 중 첫번째 인덱스 반환
SELECT SUBSTRING_INDEX("www.w3schools.com", ".", 1);

##양쪽 공백 제거
SELECT TRIM('    SQL Tutorial    ') 
    AS TrimmedString;

##대문자로 변환
SELECT UCASE("SQL Tutorial is FUN!");
SELECT UPPER("SQL Tutorial is FUN!");


##절대값 반환
SELECT ABS(-243.5);

##코사인값 반환
SELECT ACOS(0.25);

##싸인값 반환
SELECT ASIN(0.25);

##탄젠트값 반환
SELECT ATAN(2.5);

##탄젠트 2
SELECT ATAN2(0.50, 1);

##평균
SELECT AVG(Price) 
    AS AveragePrice 
  FROM Products;

##큰 정수값 반환
SELECT CEIL(25.75);

SELECT CEILING(25.75);

##코사인
SELECT COS(2);

##코탄젠트
SELECT COT(6);

##갯수 반환
SELECT COUNT(ProductID) 
    AS NumberOfProducts 
  FROM Products;

##래디안값
SELECT DEGREES(1.5);

##나누기
SELECT 10 DIV 5;


SELECT EXP(1);

##더작은 정수값 반환
SELECT FLOOR(25.75);

##가장 큰값 반환
SELECT GREATEST(3, 12, 34, 8, 25);

##최소값반환
SELECT GREATEST(3, 12, 34, 8, 25);

##로그값 반환
SELECT LN(2);
SELECT LOG(2);
SELECT LOG10(2);
SELECT LOG2(6);

#최대, 최소값
SELECT MAX(Price) 
AS LargestPrice 
FROM Products;

SELECT MIN(Price) 
AS SmallestPrice 
FROM Products;

#나눈 몫
SELECT MOD(18, 4);


#파이값 반환
SELECT PI();

#뒤의값으로 제곱
SELECT POW(2, 3);
SELECT POWER(4, 2);

##각도를 라디안 값으로 반환해주는 함수
SELECT RADIANS(180);

##랜덤하게 테이블에 저장하는 함수
SELECT RAND(6);

##반올림
SELECT ROUND(135.375, 2);


##값이 양수면 1 0이면 0 음수면 -1을 반환하는 함수
SELECT SIGN(255.5);

##사인값 반환
SELECT SIN(2);

##제곱근
SELECT SQRT(64);

###더하기
SELECT SUM(Quantity) 
AS TotalItemsOrdered 
FROM OrderDetails;

##탄젠트값 반환
SELECT TAN(1.75);

##값 지우기
SELECT TRUNCATE(135.375, 2);


##시간  더하기
SELECT ADDTIME("2017-06-15 09:34:21.000001", "2:10:5.000003");

##날짜 더하기 시간도 가능
SELECT ADDDATE("2017-06-15 09:34:21", INTERVAL 15 MINUTE);























