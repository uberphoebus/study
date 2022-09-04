/* 2021.7.21 수요일 */
 

SELECT * FROM customers;

SELECT customername, city 
  FROM customers;


SELECT customerid, customername, contactname 
  FROM customers; 
  
SELECT distinct country 
  FROM customers;
  
SELECT COUNT(DISTINCT country) 
  FROM customers;
  
SELECT COUNT(*)   
   FROM (SELECT DISTINCT country 
            FROM customers) aa ;
            
SELECT COUNT(*)
   FROM customers;
            
SELECT Count(*) AS DistinctCountries
FROM (SELECT DISTINCT Country FROM customers) aa;

#  Where 조건절 

SELECT *
  FROM customers
 WHERE substr(country,1,6) = 'Mexico'; 
 
SELECT * 
  FROM customers
 WHERE customerid = 2;
 
SELECT * 
  FROM customers
 WHERE customerid > 80;
 
SELECT * 
  FROM customers 
 WHERE customerid BETWEEN 60 AND 70;
 
SELECT * 
  FROM customers 
WHERE  customerid > 60 AND customerid < 70;

SELECT country
  FROM customers 
 WHERE country LIKE "Me%";
 
SELECT city 
  FROM customers 
  WHERE city LIKE 's%';
  
SELECT city 
  FROM customers 
  WHERE city LIKE '%o';
  
SELECT city 
  FROM customers
 WHERE city LIKE '__n%';

SELECT city
  FROM customers
 WHERE city IN ('Paris','London');
 
SELECT city 
  FROM customers
 WHERE customerid IN (10,20,30,40,50);
 
/* 2021.7.22 목요일 */ 
# 1. 09:30~

# Q&A 
# 함수 사용 
SELECT COUNT(*) 
  FROM customers;
  
SELECT customerid, city* 
  FROM customers;

# alias 별칭 사용 
SELECT COUNT(*) AS 전체row수
  FROM customers;

# 문자열 " ", ' '
SELECT city 
  FROM customers 
  WHERE city LIKE 's%';
  
SELECT city 
  FROM customers 
  WHERE city LIKE "s%";
  
/* 논리연산자 */
SELECT * 
  FROM customers
 WHERE substr(country,1,7) = "germany" 
   AND substr(city,1,6) = "berlin";
   
SELECT * 
  FROM customers
  WHERE SUBSTR(country,1,7) = "germany";
  
SELECT * 
  FROM customers
 WHERE SUBSTR(city, 1, 6) = "berlin";
 
SELECT * 
  FROM customers
 WHERE substr(city,1,6) = "berlin" 
   or substr(city,1,9) = "stuttgart";
   
SELECT * 
  FROM customers
 WHERE SUBSTR(city,1,9) = "stuttgart";
 
SELECT * 
  FROM customers
 WHERE SUBSTR(country,1,7) = "germany"
   OR  SUBSTR(country,1,5) = "Spain";
   
SELECT country AS 나라 
  FROM customers
 WHERE Not SUBSTR(country,1,7) = "germany";
 
SELECT * 
  FROM customers
 WHERE SUBSTR(country,1,7)="germany" 
   AND ( SUBSTR(city,1,6) = "berlin" 
	      OR  SUBSTR(city,1,9) = "stuttgart");	
		  
SELECT * 
  FROM customers
 WHERE SUBSTR(country,1,7)="germany" ;    

SELECT * 
  FROM customers
 WHERE ( SUBSTR(city,1,6) = "berlin" 
	      OR  SUBSTR(city,1,9) = "stuttgart");
	      
	      
SELECT country 
  FROM customers
 WHERE NOT SUBSTR(country,1,7) = "germany"
   AND NOT SUBSTR(country,1,3) = "usa";
   
# customers에서 germany가 아니고, usa가 아닌
#  나라 숫자는? 

SELECT COUNT( DISTINCT country)
  FROM customers
 WHERE NOT SUBSTR(country,1,7) = "germany"
   AND NOT SUBSTR(country,1,3) = "usa";
   
SELECT * 
  FROM customers
 WHERE SUBSTR(city,1,6) = "berlin"
   AND substr(postalcode,1,5) = "12209";
   
## 데이터 바꾸기..
# 2. 10:30~
   
SELECT * 
  FROM customers
WHERE city = "berlin";

SELECT COUNT( DISTINCT country)
  FROM customers
 WHERE NOT country = "germany"
   AND NOT country = "usa";

DESC customers;

## ORDER BY 
SELECT * 
  FROM customers
 ORDER BY country desc;
 
SELECT country, customername 
  FROM customers
 ORDER BY country, customername;
 
SELECT country, customername 
  FROM customers
 ORDER BY country, customername ;
 
# default 기능..  order by asc 

# INSERT INTO 
INSERT INTO customers (customername, contactname, 
                      address, city, postalcode, country)
    VALUES ('Cardinal','Tom b.Erichsen','Skagen 21',
               'Stavanger','4006','Norway');
               
SELECT customername, contactname, address
 FROM customers
 WHERE address IS NULL; 
 
SELECT customername, contactname, address
 FROM customers
 WHERE address IS NOT NULL; 
 
SELECT customerid, contactname, city
 FROM customers
 WHERE customerid = 1;
 
UPDATE customers
 SET contactname = "Alfred Schmidt",
     city = "Frankfurt" 
 WHERE customerid = 1;
 
SELECT customerid, contactname, city
 FROM customers
 WHERE customerid = 1;
 
# update 전에 대상 확인
SELECT postalcode 
  FROM customers
WHERE country = "Mexico";

# update 문 실행 
UPDATE customers 
  SET  postalcode = "00000"
  WHERE country = "Mexico";
  
# update 후 확인 
SELECT postalcode 
  FROM customers
WHERE country = "Mexico";

/* Delete 문 */

SELECT *
  FROM customers
 WHERE customername = "alfreds Futterkiste";
 
DELETE FROM customers 
 WHERE customername = "alfreds Futterkiste";
 
SELECT *
  FROM customers
 WHERE customername = "alfreds Futterkiste";
 
SELECT * 
  FROM customers;
  
SELECT * 
  FROM customers
  LIMIT 3;
  
SELECT * 
  FROM customers
 WHERE country = "germany";
 
SELECT * 
  FROM customers
 WHERE country = "germany"
 LIMIT 3;
 
# 3. 
/* min(), max() 함수funciton */

select min(price) AS 최저가,
       MAX(price) AS 최고가
 FROM products;
 
SELECT COUNT(productid) AS 제품수 ,
       AVG(price) AS 평균,
       MIN(price) AS 최저가, 
       MAX(price) AS 최고가 
  FROM products; 
  
SELECT COUNT(productid) AS '제품수' ,
       AVG(price) AS '평균',
       MIN(price) AS '최저가', 
       MAX(price) AS '최고가' 
  FROM products; 
  
SELECT *
  FROM order_details;
  
SELECT SUM(quantity)
  FROM order_details;
  
SELECT *
  FROM customers
 WHERE country IN ('germany','france','uk');
 
SELECT * 
  FROM customers
 WHERE country = 'germany' 
   OR  country = 'france'
   OR  country = 'uk'
   
SELECT * 
  FROM customers
 WHERE country IN ( SELECT distinct country 
                      FROM customers
                      WHERE country = 'germany'
                        OR  country = 'france'
                        OR  country = 'uk');
                        
SELECT * 
  FROM customers
 WHERE country IN (SELECT distinct country
                     FROM suppliers); 
                     
SELECT * 
  FROM products 
 WHERE price BETWEEN 10 AND 20;
 
SELECT * 
  FROM products
 WHERE price >= 10 
   AND price <= 20;
   
SELECT customername, 
       CONCAT_WS(', ',address,postalcode,city,country) 
  FROM customers;
   
SELECT customername, 
       CONCAT_WS(', ',address,postalcode,city,country) AS address
  FROM customers;
  
SELECT customername, 
       CONCAT_WS(address,postalcode,city,country) AS address
  FROM customers;

SELECT o.orderid, o.orderdate, c.customername
  FROM customers AS c, orders AS o
WHERE  c.customername = 'Around the Horn' 
  AND  c.CustomerID = o.customerid;
  
SELECT ooo.orderid, ooo.orderdate, ccc.customername
  FROM customers AS ccc, orders AS ooo
WHERE  ccc.customername = 'Around the Horn' 
  AND  ccc.CustomerID = ooo.customerid ;  
  
SELECT * FROM customers;

SELECT * FROM orders;

### join 
# 4. 

SELECT orders.orderid, 
       customers.customername,
       orders.OrderDate
 FROM orders
 INNER JOIN customers 
       ON orders.CustomerID = customers.CustomerID
 ORDER BY orders.orderid; 
       
SELECT orders.orderid,
       orders.OrderDate
 FROM orders
 ORDER BY orders.orderid;
 
SELECT o.orderid,o.OrderDate, c.customername
 FROM orders o, customers c
WHERE o.CustomerID = c.CustomerID
 ORDER BY o.orderid;
 
SELECT Orders.OrderID, Customers.CustomerName, Shippers.ShipperName
FROM ((Orders
INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID)
INNER JOIN Shippers ON Orders.ShipperID = Shippers.ShipperID);

SELECT Customers.CustomerName, Orders.OrderID
FROM Customers
LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID
ORDER BY Customers.CustomerName;

SELECT Customers.CustomerName, Orders.OrderID
FROM customers, orders 
WHERE customers.CustomerID = orders.customerid 
ORDER BY Customers.CustomerName;

SELECT Orders.OrderID, Employees.LastName, Employees.FirstName
FROM Orders
RIGHT JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID
ORDER BY Orders.OrderID;

SELECT Customers.CustomerName, Orders.OrderID
FROM Customers
CROSS JOIN orders;

SELECT Customers.CustomerName, Orders.OrderID
FROM Customers
CROSS JOIN Orders
WHERE Customers.CustomerID=Orders.CustomerID;

SELECT A.CustomerName AS CustomerName1, B.CustomerName AS CustomerName2, A.City
FROM Customers A, Customers B
WHERE A.CustomerID <> B.CustomerID
AND A.City = B.City
ORDER BY A.City;

SELECT City FROM Customers
UNION
SELECT City FROM Suppliers
ORDER BY City;

SELECT City FROM Customers
UNION ALL
SELECT City FROM Suppliers
ORDER BY City;

SELECT City, Country FROM Customers
WHERE Country='Germany'
UNION
SELECT City, Country FROM Suppliers
WHERE Country='Germany'
ORDER BY City;

SELECT City, Country FROM Customers
WHERE Country='Germany'
UNION ALL
SELECT City, Country FROM Suppliers
WHERE Country='Germany'
ORDER BY City;

SELECT COUNT(customerid), country
 FROM customers
 GROUP BY country;
 
SELECT country, COUNT(customerid)
 FROM customers
 GROUP BY country; 

SELECT country, COUNT(customerid)
 FROM customers
 GROUP BY country
 ORDER BY COUNT(customerid) desc
 LIMIT 3; 
 
SELECT Shippers.ShipperName, COUNT(Orders.OrderID) AS NumberOfOrders FROM Orders
LEFT JOIN Shippers ON Orders.ShipperID = Shippers.ShipperID
GROUP BY ShipperName;
 
 
# 5. 
SELECT country, COUNT(customerid)
FROM customers
GROUP BY country 
HAVING COUNT(customerid) > 5
ORDER BY COUNT(customerid) DESC
LIMIT 3;

SELECT Employees.LastName, COUNT(Orders.OrderID) AS NumberOfOrders
  FROM ( orders
         INNER JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID)
GROUP BY LastName
HAVING COUNT(Orders.OrderID) > 10;

SELECT Employees.LastName, COUNT(Orders.OrderID) AS NumberOfOrders
  FROM ( orders
         INNER JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID)
GROUP BY LastName
HAVING NumberOfOrders > 10;

SELECT * FROM orders;

SELECT a.employeeid, COUNT(a.orderid), b.LastName
  FROM orders a, employees b
 WHERE a.EmployeeID = b.EmployeeID
GROUP BY a.employeeid;
 
SELECT SupplierName
FROM Suppliers
WHERE EXISTS 
      (SELECT ProductName 
		   FROM Products 
			WHERE Products.SupplierID = Suppliers.supplierID
			  AND Price = 22);
			  
SELECT suppliername
  FROM suppliers;
  
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
  WHERE Quantity > 99);   
  
SELECT productname 
  FROM products
 WHERE price < 20;
 
SELECT ProductName
FROM Products
WHERE ProductID = ANY
  (SELECT ProductID
  FROM Order_Details
  WHERE Quantity > 1000); 
  
INSERT INTO Customers (CustomerName, City, Country)
SELECT SupplierName, City, Country FROM suppliers;

SELECT COUNT(*) FROM customers;

SELECT * FROM customers;

SELECT OrderID, Quantity,
CASE
    WHEN Quantity > 30 THEN '30이상'
    WHEN Quantity = 30 THEN '정확히30'
    ELSE '30이하'
END AS QuantityText
FROM order_details;

SELECT OrderID, Quantity,
CASE
    WHEN Quantity > 30 THEN 100
    WHEN Quantity = 30 THEN 120
    ELSE 150
END AS price
FROM order_details;

SELECT OrderID, Quantity,
CASE
    WHEN Quantity > 30 THEN quantity * 100
    WHEN Quantity = 30 THEN quantity * 120
    ELSE quantity * 150
END AS amount 
FROM order_details;

SELECT CustomerName, City, Country
FROM Customers
ORDER BY (CASE
             WHEN City IS NULL THEN Country
             ELSE City
          END);
          
SELECT * 
  FROM customers
  WHERE city IS NULL; 
  
# 제품명과 단가 * 
SELECT ProductName, UnitPrice * (UnitsInStock + UnitsOnOrder)
FROM products; -- 제품테이플 

SELECT * 
 FROM products;
 
-- dfkdaf daf 
# fdkalfja dfdl
/* dfadaf */ 
SELECT   -- 설명붙일때 

SELECT 17 % 5;