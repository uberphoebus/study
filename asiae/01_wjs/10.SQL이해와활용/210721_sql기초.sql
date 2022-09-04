SELECT * FROM user;

SELECT * FROM help_category;

# DataBase 생성 
CREATE DATABASE testDB;


# DataBase 삭제
# DROP DATABASE testDB;  

# Table 생성 

#
-- 내용 
/* 내용 */

CREATE TABLE test_tbl
        ( id           INT,
          class        VARCHAR(3),
          my_date      date,
          remark       varchar(10),
         PRIMARY KEY (id) );
         
/* 테이블 삭제하기 */
DROP TABLE test_tbl;

#기존 테이블이 존재하면 실행하지 말고
# 테이블이 없으면 생성하라 
CREATE TABLE if not exists test_tbl  
        ( id           INT,
          class        VARCHAR(3),
          my_date      date,
          remark       varchar(10),
         PRIMARY KEY (id) );


ALTER TABLE test_tbl 
  MODIFY class VARCHAR(5);
  
DESC test_tbl;
 
1, "A", "2021-07-21", "하나"
INSERT INTO test_tbl VALUES (1,"A","2021-07-21","하나");
INSERT INTO test_tbl (id, class, my_date, remark) 
            VALUES (2, "B", "2021-07-21","둘");             
INSERT INTO test_tbl VALUES (3,"C","2021-07-21","33"); 
INSERT INTO test_tbl (id, class, remark) 
            VALUES (4, "D", "444"); 
            

(실습) w3schoolDB 만들고 테이블 생성하기 

# DataBase 생성 
CREATE DATABASE if not exists w3schoolDB;

CREATE TABLE if not exists customers 
        ( customerid    INT,
		    customername  VARCHAR(30),
          contactname   VARCHAR(20),
			 address       VARCHAR(30),
			 city          VARCHAR(30),
          postalcode    VARCHAR(10),
			 country       VARCHAR(20),
         PRIMARY KEY (customerid) );  
			
ALTER TABLE customers
  MODIFY contactname VARCHAR(30);			     

INSERT INTO customers VALUES ( 89, "White Clover",
                         "Karl Jab","305-14th", "seattle",
								 "98128", "USA");
INSERT INTO customers VALUES ( 90, "Wilman Kala", 
                        "Matti","Kesku 45", "Helsinki",
                        "21240", "Finland");
INSERT INTO customers VALUES ( 91, "Wolski", 
                        "Zbyszek","Filtrowa 68", "Walla",
                        "01-012", "Poland");            

# 특정 데이터 변경 작업 
UPDATE Customers
SET ContactName = 'Alfred', City= 'Frankfurt'
WHERE CustomerID = 89;

# 특정 데이터 삭제 
DELETE FROM customers 
 WHERE customerid = 92;
 
 
 
# 실습 customers.csv import 하기 
CREATE TABLE if not exists customers 
        ( CustomerID    INT,
		    CustomerName  VARCHAR(50),
          ContactName   VARCHAR(50),
			 Address       VARCHAR(50),
			 City          VARCHAR(50),
          PostalCode    VARCHAR(50),
			 Country       VARCHAR(50),
         PRIMARY KEY (CustomerID) ); 
         
CREATE TABLE if not exists customers03 
        ( CustomerID    INT,
		    CustomerName  VARCHAR(50),
          ContactName   VARCHAR(50),
			 Address       VARCHAR(50),
			 City          VARCHAR(50),
          PostalCode    VARCHAR(50),
			 Country       VARCHAR(50),
         PRIMARY KEY (CustomerID) ); 
         
         
CREATE TABLE if not exists customers02 
        ( customerid    INT,
		    customername  VARCHAR(50),
          contactname   VARCHAR(50),
			 address       VARCHAR(50),
			 city          VARCHAR(50),
          postalcode    VARCHAR(50),
			 country       VARCHAR(50),
         PRIMARY KEY (customerid) );