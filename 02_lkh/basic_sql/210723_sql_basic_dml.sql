
# 기본 문법
-- 대소문자 구분 없음
-- 명령을 마무리 할 때는 ;
-- 띄어쓰기, 줄 바꿈 무시

# 주석 처리 방법
# 내용
-- 내용
/* 내용 */

# db 생성
CREATE DATABASE testdb;

# db 삭제
DROP DATABASE testdb;

# db내 tb 생성
CREATE TABLE test_tb1
	(id		INT,
	class		VARCHAR(3),
	my_date	DATE,
	remark	VARCHAR(10),
	PRIMARY KEY (id) );
-- 컬럼 사이 콤마(,)로 구분
-- 스크립트를 저장하고 수정 활용

# tb 삭제
DROP TABLE test_tb1;

# truncate; 틀은 유지, 데이터만 삭제
TRUNCATE TABLE test_tb1;

# 기존 tb가 없다면 생성
CREATE TABLE if not exists test_tb1
	(id		INT,
	class		VARCHAR(3),
	my_date	DATE,
	remark	VARCHAR(10),
	PRIMARY KEY (id) );

# 컬럼 수정
ALTER TABLE test_tb1
MODIFY class VARCHAR(5);

# 데이터 출력
DESC test_tb1;

# 데이터 입력
INSERT INTO test_tb1
	VALUES (1,'a','2021-07-21','하나');

INSERT INTO test_tb1 (id, class, my_date, remark)
	VALUES (2,'b','2021-07-21','둘');

INSERT INTO test_tb1 
	VALUES (3,'c','2021-07-21','세째');

INSERT INTO test_tb1 (id, class, remark)
	VALUES (4,'d','44');

INSERT INTO test_tb1 (class, remark)
	VALUES ();
-- 프라이머리 키가 없는 경우 입력 불가

# 실습

CREATE DATABASE w3schoolDB;

CREATE TABLE customers
	( customerid	INT,
	customername	VARCHAR(30),
	contactname		VARCHAR(30),
	address			VARCHAR(30),
	city				VARCHAR(30),
	postalcode		VARCHAR(10),
	country			VARCHAR(10),
	PRIMARY KEY (customerid) );

INSERT INTO customers
	VALUES(89, 'White Clover Markets', 
	'Karl Jablonki', '305 - 14th Ave. S. Suite 3B',
	'Seattle', '98128', 'USA');
INSERT INTO customers
	VALUES(90, 'Wilman Kala', 
	'Matti Karttunen', 'Keskuskatu 45',
	'Helsinki', '21240', 'Finland');
INSERT INTO customers	
	VALUES(91, 'Wolski', 
	'Zbyszek', 'ul. Fitrowa 68', 
	'Walla', '01-012', 'Poland');

# 특정 데이터 수정 update
UPDATE customers
	SET contactname = 'Alfred Schmidt', 
		city = 'Frankfurt'
	WHERE customerid = 89;
-- where 조건. 없으면 전체 수정

# 특정 데이터 삭제 delete
DELETE FROM customers WHERE customerid = 92;

# 실습 customers.csv import
DROP TABLE customers

CREATE TABLE if not exists customers
	( CustomerID	INT,
	CustomerName	VARCHAR(50),
	ContactName		VARCHAR(50),
	Address			VARCHAR(50),
	City				VARCHAR(50),
	PostalCode		VARCHAR(50),
	Country			VARCHAR(30),
	PRIMARY KEY (CustomerID) );


# 데이터 조회
SELECT * FROM customers;
-- *는 전체에 대한 것을 출력
-- * 대신 원하는 컬럼 입력 가능

SELECT customername, city
	FROM customers;
-- 컬럼명 대소문자 구분 없음

SELECT customerid, customername, contactname
	FROM customers;

# distinct 중복을 배제하고 조회
SELECT DISTINCT country
	FROM customers;
-- 특정 컬럼 지정. 전체는 불가능.

# count 함수
SELECT COUNT(DISTINCT country)
	FROM customers;

# 서브쿼리; () 내부를 임시로 tb화
SELECT COUNT(*)
	FROM (SELECT DISTINCT country
		FROM customers) aa ;

# where 조건절; select, update, delete에서
SELECT *
	FROM customers
	WHERE customerid >= 80;
-- = > < >= <= <> between like in

# between; 사이
SELECT *
	FROM customers
	WHERE customerid BETWEEN 60 AND 70;

SELECT *
	FROM customers
	WHERE country LIKE 'me%';
-- % 앞의 문자로 시작, me로 시작하는

SELECT *
	FROM customers
	WHERE city LIKE 's%';
-- s로 시작하는

SELECT city
	FROM customers
	WHERE city LIKE '%o';
-- o로 끝나는

SELECT city
	FROM customers
	WHERE city LIKE '__n%';
-- 앞 두 칸을 모를 때 _(언더바)

# in; 데이터를 만족하는지 체크

SELECT city
	FROM customers
	WHERE city IN ('Paris','london');

SELECT city
	FROM customers
	WHERE customerid IN (10,20,30,40,50);


/* 21.07.22. */

# Q&A
# 함수의 띄어쓰기
SELECT COUNT(*)
	FROM customers;
-- count (*) 는 인식을 못함

# alias 별칭 사용
SELECT COUNT(*) AS 전체row수
	FROM customers;
-- count() 함수 뒤를 별칭 적용
-- [AS] 생략 가능

# and, or, not 조건절
SELECT * FROM customers
	WHERE country = 'germany'
		AND city = 'berlin';

SELECT * FROM customers
	WHERE country = 'germany';

SELECT * FROM customers
	WHERE country = 'berlin';
-- 두 명령의 교집합을 조회

SELECT * FROM customers
	WHERE city = 'berlin'
		OR city = 'stuttgart';
-- 합집합

SELECT * FROM customers
	WHERE country = 'germany'
		OR country = 'spain'

SELECT country fROM customers
	WHERE not country = 'germany';

SELECT * FROM customers
	WHERE country = 'germany'
		AND ( city = 'berlin'
				or city = 'stuttgart' );
-- 소괄호 활용

SELECT * FROM customers
	WHERE not SUBSTR(country,1,7) = 'germany'
			AND NOT SUBSTR(country,1,3) = 'usa';

# 나라 중복 제거
SELECT COUNT(DISTINCT country) FROM customers
	WHERE NOT country = 'germany'
			AND NOT country = 'usa';
-- 출력 컬럼 앞에 distinct

# w3 excercise
SELECT * FROM customers
	WHERE city = 'berlin'
			AND postalcode = '12209';

# substr(str, pos, len)
-- 문자 단위로 문자열을 자름
-- str 문자열, pos 시작지점, len 길이

# 컬럼 순서 설정(오름차순, 내림차순)
SELECT * FROM customers
	ORDER BY country desc;
-- 기본은 asc, 역순은 desc

SELECT country, customername FROM customers
	ORDER BY country asc, customername desc;
-- 두 컬럼도 순서대로 정렬
-- 별도로 역순 설정 가능

# insert into
INSERT INTO customers (customername, contactname,
							address, city, 
							postalcode, country)
	VALUES('Cardinal', 'Tom b.Erichsen', 
			'Skagen 21', 'Stavanger', 
			'4006', 'Norway');

# null
SELECT customername, contactname, address
	FROM customers
	WHERE address IS not NULL;

# update; 수정 전후로 데이터 확인
SELECT customerid, contactname, city
	FROM customers
	WHERE customerid = 1;
-- 먼저 확인하고
UPDATE customers
	SET contactname = 'Alfred Schmidt',
		city = 'Frankfurt'
	WHERE customerid = 1;
-- 확인하고 수정하고 다시 확인

SELECT postalcode FROM customers
	WHERE country = 'mexico';
-- 멕시코 5건 확인

UPDATE customers
	SET postalcode = '00000'
	WHERE country = 'mexico';
-- 멕시코 우편번호 수정
-- where 조건을 입력하지 않으면 전체 수정

# 삭제; 전후로 데이터 확인
SELECT * FROM customers
	WHERE customername = 'Alfreds Futterkiste'
-- 확인
DELETE FROM customers
	WHERE customername = 'Alfreds Futterkiste'
-- 확인 후 삭제

# limit; 상위권 조회
SELECT * FROM customers
	LIMIT 5;
-- limit가 없으면 전체 조회

SELECT * FROM customers
	WHERE country = 'germany'
	LIMIT 4;
-- germany 중 상위 4건 조회

# min, max function
SELECT min(price) as 최저가,
		max(price) as 최고가
	FROM products;
-- 여러 줄도 ,로 구분하여 가능

# count, avg, sum
SELECT COUNT(productid) AS 제품수,
		AVG(price) AS 평균가,
		MIN(price) AS 최저가,
		MAX(price) AS 최고가
	FROM products;
-- [AS] 뒤는 띄어쓰기 불가능

SELECT * FROM order_details;

SELECT SUM(quantity) FROM order_details;

# wildcards; 숨겨진 문자, 자습

# in; 선택 조회
SELECT * FROM customers
	WHERE country IN ('germany', 'france', 'uk');
-- or 구문을 단순하게 쓸 수 있음

SELECT * FROM customers
	WHERE country = 'germany'
			OR country = 'france'
			OR country = 'uk';
-- in과 같은 기능

SELECT * FROM customers
	WHERE country IN ( SELECT country FROM customers
								WHERE country = 'germany'
									OR country = 'france'
									OR country = 'uk' );

SELECT * FROM customers
	WHERE country
		IN ( SELECT country FROM suppliers );
-- supt tb에 있는 나라들 출력

# between; ~이상, ~이하
SELECT * FROM products
	WHERE price BETWEEN 10 AND 20;

SELECT * FROM products
	WHERE price >= 10 AND price <= 20;

# alias; tb, cl의 별칭 설정
SELECT customername,
	CONCAT_WS(', ', address, postalcode, city, country) AS address
	FROM customers;
-- concat_ws는 컬럼을 합치는 기능

SELECT o.orderid, o.orderdate, c.customername
	FROM customers AS c, orders AS o
	WHERE c.customername = 'Around the Horn'
	AND c.CustomerID = o.customerid;
-- tb도 alias 적용 가능
-- customerid가 두 tb에 있으므로 구분
-- cus를 c로, order는 o로 정함
-- 테이블 별칭과 컬럼 사이에 . 으로 
-- 어려우므로 복습 여러번
SELECT * FROM customers;
SELECT * FROM orders;

# joins; 중요
-- 2개의 데이터셋을 어떻게 처리할지에 대한 옵션
-- innerjoin 중복된, 공통 데이터
-- leftjoin a에만 있는 데이터
-- rightjoin b에만 있는 데이터
-- crossjoin 둘 다에 있는 데이터

# inner join
SELECT orders.OrderID,
		 customers.customername,
		 orders.orderdate
	FROM orders
	INNER JOIN customers
		ON orders.customerid = customers.customerid;
-- select가 기준, from은 가져오는 곳
-- 앞을 기준으로 하되 뒤를 참조

SELECT o.OrderID, c.customername, o.orderdate
	FROM orders o, customers c
	WHERE o.customerid = c.customerid
		ORDER BY o.orderid;
-- 위와 같은 출력

SELECT Orders.OrderID, Customers.CustomerName, Shippers.ShipperName
	FROM ((Orders
	INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID)
	INNER JOIN Shippers ON Orders.ShipperID = Shippers.ShipperID);
-- 예시 복습
-- 마스터테이블을 갖고 있어서 수정할 때 참조

# left join

SELECT Customers.CustomerName, Orders.OrderID
FROM Customers
LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID
ORDER BY Customers.CustomerName;
-- cus 테이블 기준
-- orderid가 없어도 진행

SELECT Customers.CustomerName, Orders.OrderID
FROM customers, orders
WHERE customers.CustomerID = orders.customerid
ORDER BY Customers.CustomerName;
-- orderid가 없으면 제외

# right join

SELECT Orders.OrderID, Employees.LastName, Employees.FirstName
FROM Orders
RIGHT JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID
ORDER BY Orders.OrderID;
-- orderid가 비어도 출력

# cross join; 곱

SELECT Customers.CustomerName, Orders.OrderID
FROM Customers
CROSS JOIN Orders;

SELECT Customers.CustomerName, Orders.OrderID
FROM Customers
CROSS JOIN Orders
WHERE Customers.CustomerID=Orders.CustomerID;

# self join
-- 같은 tb에서 명칭을 다르게 줘서 구분
-- 다른 tb처럼 여기도록

SELECT A.CustomerName AS CustomerName1, B.CustomerName AS CustomerName2, A.City
FROM Customers A, Customers B
WHERE A.CustomerID <> B.CustomerID
AND A.City = B.City
ORDER BY A.City;
-- 고객id가 다르면서
-- 같은 시에 있는

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# union; 데이터 합병

SELECT City FROM Customers
UNION
SELECT City FROM Suppliers
ORDER BY City;
-- 더하지만 중복은 제외

SELECT City FROM Customers
UNION ALL
SELECT City FROM Suppliers
ORDER BY City;
-- 더하면서 중복돼도 출력

SELECT City, Country FROM Customers
WHERE Country='Germany'
UNION
SELECT City, Country FROM Suppliers
WHERE Country='Germany'
ORDER BY City;
-- 중복 제외

SELECT City, Country FROM Customers
WHERE Country='Germany'
UNION ALL
SELECT City, Country FROM Suppliers
WHERE Country='Germany'
ORDER BY City;
-- 중복 포함

# group by

SELECT country, COUNT(customerid)
	FROM customers
	GROUP BY country;
-- 데이터 집계

SELECT country, COUNT(customerid)
	FROM customers
	GROUP BY country
	ORDER BY COUNT(customerid) DESC
	LIMIT 3;
-- 집계 데이터를 정렬하고, 상위권

SELECT Shippers.ShipperName, COUNT(Orders.OrderID) AS NumberOfOrders FROM Orders
LEFT JOIN Shippers ON Orders.ShipperID = Shippers.ShipperID
GROUP BY ShipperName;

# having;
-- where는 tb 안에서 조건을 형성
-- having은 그룹함수에 대한 조건

SELECT country, COUNT(customerid) FROM customers
	GROUP BY country
	HAVING COUNT(customerid) > 5
	ORDER BY COUNT(customerid) DESC
	LIMIT 3;
-- count에 대한 조건

SELECT Employees.LastName, COUNT(Orders.OrderID) AS NumberOfOrders
	FROM (Orders
			INNER JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID)
GROUP BY LastName
HAVING COUNT(Orders.OrderID) > 10;

SELECT a.employeeid, COUNT(orderid)
	FROM orders a, employees b
	WHERE a.employeeid = b.employeeid
	GROUP BY a.employeeid;
-- 위에서 having 조건 제외

# exists

SELECT suppliername FROM suppliers
	WHERE EXISTS
		(SELECT productname FROM products
			WHERE products.supplierid = suppliers.supplierid
				AND price < 10);

# any, all
-- any는 동일할 때 출력
-- all은 전체

SELECT ProductName
FROM Products
WHERE ProductID = ANY
  (SELECT ProductID
  FROM Order_Details
  WHERE Quantity = 10);

SELECT ProductName
FROM Products
WHERE ProductID = ALL
  (SELECT ProductID
  FROM Order_Details
  WHERE Quantity = 10);

# 다른 테이블의 값 가져오기
INSERT INTO Customers (CustomerName, City, Country)
SELECT SupplierName, City, Country FROM suppliers;
-- 필요한 데이터만 추출

# case; 오라클과 다른 부분(decode), if문

SELECT OrderID, Quantity,
CASE
    WHEN Quantity > 30 THEN 100
    WHEN Quantity = 30 THEN 120
    ELSE 150
END AS price
FROM Order_Details;

# null function; db와 사이트 db가 다름

SELECT ProductName, UnitPrice * (UnitsInStock + UnitsOnOrder)
FROM Products;

# ifnull(cl, n); cl이 null이면 n으로 치환

# coalesce(cl, n); 


# data type
-- char(s); 고정된 자릿수
-- varchar(s); 다양한 자릿수
-- binary(s); 바이너리 값으로 저장
-- 바이너리는 비트 단위로 계산하는 것
-- varbin
-- blob(s); 큰 바이너리

-- bit
-- tinyint(s)
-- bool; T F
-- int(s)
-- float(s, d); 자주 사용
-- decimal(s, d); 전체 사이즈, 소수 사이즈

-- 

# 모두의 SQL 데이터베이스 작성
# job_history, locations 자료 불러오기 오류

CREATE TABLE Countries
	( country_id	CHAR(2),
	country_name	VARCHAR(40),
	region_id		INT(11),
	PRIMARY KEY (country_id) );

CREATE TABLE Departments
	( department_id	INT(4),
	department_name	VARCHAR(30),
	manager_id			INT(6),
	location_id			INT(4),
	PRIMARY KEY (department_id) );

CREATE TABLE Employees
	( employee_id		INT(6),
	first_name			VARCHAR(20),
	last_name			VARCHAR(25),
	email					VARCHAR(25),
	phone_number		VARCHAR(20),
	hire_date			DATE,
	job_id				VARCHAR(10),
	salary				DECIMAL(8,2),
	commission_pct		DECIMAL(2,2),
	manager_id			INT(6),
	department_id		INT(4),
	PRIMARY KEY (employee_id) );

CREATE TABLE job
	( job_id				VARCHAR(10),
	job_title			VARCHAR(35),
	min_salary			INT(6),
	max_salary			INT(6),
	PRIMARY KEY (job_id) );

CREATE TABLE Job_history
	( employee_id		INT(6),
	start_date			DATE,
	end_date				DATE,
	job_id				VARCHAR(10),
	department_id		INT(4),
	PRIMARY KEY (employee_id, start_date) );

Insert into modu_sql.JOB_HISTORY (EMPLOYEE_ID,START_DATE,END_DATE,JOB_ID,DEPARTMENT_ID) values (102,date_format('01/01/13','%y/%m/%d'),date_format('06/07/24','%y/%m/%d'),'IT_PROG',60);
Insert into modu_sql.JOB_HISTORY (EMPLOYEE_ID,START_DATE,END_DATE,JOB_ID,DEPARTMENT_ID) values (101,date_format('97/09/21','%y/%m/%d'),date_format('01/10/27','%y/%m/%d'),'AC_ACCOUNT',110);
Insert into modu_sql.JOB_HISTORY (EMPLOYEE_ID,START_DATE,END_DATE,JOB_ID,DEPARTMENT_ID) values (101,date_format('01/10/28','%y/%m/%d'),date_format('05/03/15','%y/%m/%d'),'AC_MGR',110);
Insert into modu_sql.JOB_HISTORY (EMPLOYEE_ID,START_DATE,END_DATE,JOB_ID,DEPARTMENT_ID) values (201,date_format('04/02/17','%y/%m/%d'),date_format('07/12/19','%y/%m/%d'),'MK_REP',20);
Insert into modu_sql.JOB_HISTORY (EMPLOYEE_ID,START_DATE,END_DATE,JOB_ID,DEPARTMENT_ID) values (114,date_format('06/03/24','%y/%m/%d'),date_format('07/12/31','%y/%m/%d'),'ST_CLERK',50);
Insert into modu_sql.JOB_HISTORY (EMPLOYEE_ID,START_DATE,END_DATE,JOB_ID,DEPARTMENT_ID) values (122,date_format('07/01/01','%y/%m/%d'),date_format('07/12/31','%y/%m/%d'),'ST_CLERK',50);
Insert into modu_sql.JOB_HISTORY (EMPLOYEE_ID,START_DATE,END_DATE,JOB_ID,DEPARTMENT_ID) values (200,date_format('95/09/17','%y/%m/%d'),date_format('01/06/17','%y/%m/%d'),'AD_ASST',90);
Insert into modu_sql.JOB_HISTORY (EMPLOYEE_ID,START_DATE,END_DATE,JOB_ID,DEPARTMENT_ID) values (176,date_format('06/03/24','%y/%m/%d'),date_format('06/12/31','%y/%m/%d'),'SA_REP',80);
Insert into modu_sql.JOB_HISTORY (EMPLOYEE_ID,START_DATE,END_DATE,JOB_ID,DEPARTMENT_ID) values (176,date_format('07/01/01','%y/%m/%d'),date_format('07/12/31','%y/%m/%d'),'SA_MAN',80);
Insert into modu_sql.JOB_HISTORY (EMPLOYEE_ID,START_DATE,END_DATE,JOB_ID,DEPARTMENT_ID) values (200,date_format('02/07/01','%y/%m/%d'),date_format('06/12/31','%y/%m/%d'),'AC_ACCOUNT',90);

CREATE TABLE locations
	( location_id		INT(4),
	street_address		VARCHAR(40),
	postal_code			VARCHAR(12),
	city					VARCHAR(30),
	state_province		VARCHAR(25),
	country_id			CHAR(2),
	PRIMARY KEY (location_id) );

INSERT INTO locations VALUES(1000,"1297 Via Cola di Rie","00989","Roma","","IT"
)
INSERT INTO locations VALUES(1100,"93091 Calle della Testa","10934","Venice","","IT"
)
INSERT INTO locations VALUES(1200,"2017 Shinjuku-ku","1689","Tokyo","Tokyo Prefecture","JP"
)
INSERT INTO locations VALUES(1300,"9450 Kamiya-cho","6823","Hiroshima","","JP"
)
INSERT INTO locations VALUES(1400,"2014 Jabberwocky Rd","26192","Southlake","Texas","US"
)
INSERT INTO locations VALUES(1500,"2011 Interiors Blvd","99236","South San Francisco","California","US"
)
INSERT INTO locations VALUES(1600,"2007 Zagora St","50090","South Brunswick","New Jersey","US"
)
INSERT INTO locations VALUES(1700,"2004 Charade Rd","98199","Seattle","Washington","US"
)
INSERT INTO locations VALUES(1800,"147 Spadina Ave","M5V 2L7","Toronto","Ontario","CA"
)
INSERT INTO locations VALUES(1900,"6092 Boxwood St","YSW 9T2","Whitehorse","Yukon","CA"
)
INSERT INTO locations VALUES(2000,"40-5-12 Laogianggen","190518","Beijing","","CN"
)
INSERT INTO locations VALUES(2100,"1298 Vileparle (E)","490231","Bombay","Maharashtra","IN"
)
INSERT INTO locations VALUES(2200,"12-98 Victoria Street","2901","Sydney","New South Wales","AU"
)
INSERT INTO locations VALUES(2300,"198 Clementi North","540198","Singapore","","SG"
)
INSERT INTO locations VALUES(2400,"8204 Arthur St","","London","","UK"
)
INSERT INTO locations VALUES(2500,"Magdalen Centre, The Oxford Science Park","OX9 9ZB","Oxford","Oxford","UK"
)
INSERT INTO locations VALUES(2600,"9702 Chester Road","09629850293","Stretford","Manchester","UK"
)
INSERT INTO locations VALUES(2700,"Schwanthalerstr. 7031","80925","Munich","Bavaria","DE"
)
INSERT INTO locations VALUES(2800,"Rua Frei Caneca 1360 ","01307-002","Sao Paulo","Sao Paulo","BR"
)
INSERT INTO locations VALUES(2900,"20 Rue des Corps-Saints","1730","Geneva","Geneve","CH"
)
INSERT INTO locations VALUES(3000,"Murtenstrasse 921","3095","Bern","BE","CH"
)
INSERT INTO locations VALUES(3100,"Pieter Breughelstraat 837","3029SK","Utrecht","Utrecht","NL"
)
INSERT INTO locations VALUES(3200,"Mariano Escobedo 9991","11932","Mexico City","Distrito Federal,","MX");



CREATE TABLE regions
	( region_id			INT(11),
	region_name			VARCHAR(25) );

CREATE TABLE Sample_product
	( product_id		INT(11),
	product_name		VARCHAR(30),
	manu_date			DATE,
	factory				VARCHAR(10) );

TRUNCATE TABLE job_history;

TRUNCATE TABLE locations;


# 데이터 업로드 시 주의사항
-- 경로에 한글이 없도록. 가능한 컴퓨터 이름도
-- charset


##################################################

