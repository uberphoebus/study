/* SQL 함수, function */

SELECT customername AS aa
 FROM  customers;
 
SELECT ascii(customername) AS aa
 FROM  customers;
 
SELECT ASCII('A');

SELECT CHAR_LENGTH("SQL Tutorial") 

SELECT customername, CHAR_LENGTH(customername) 
  FROM customers
WHERE  CHAR_LENGTH(customername) > 30;

SELECT CONCAT("SQL ", "Tutorial ", "is ", "fun!") AS aa;

SELECT * FROM customers;

SELECT CONCAT(customername, '-', contactname)
  FROM customers;
  
SELECT FIELD("q", "s", "q", "l");

SELECT FIELD("Q", "s", "q", "l");

SELECT FIELD("c", "a", "b");

SELECT FIND_IN_SET("a", "s,q,l");

SELECT FORMAT(250500.5634, 2);

SELECT INSERT("W3Schools.com", 1, 9, "Example");

SELECT INSTR("W3Schools.com", "3") AS MatchPosition;

