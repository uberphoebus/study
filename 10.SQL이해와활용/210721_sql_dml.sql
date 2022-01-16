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