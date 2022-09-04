# ASCII
SELECT CustomerName, ASCII(CustomerName) AS 진우선
	FROM customers;


# CHAR_LENGTH - as 뒤에 문자갯수 계산
SELECT CHAR_LENGTH("SQL Tutorial") AS Length_Of_String;


# CHARACTER_LENGTH - as 뒤에 문자갯수 계산
SELECT CHARACTER_LENGTH("SQL Tutorial") AS Game_of_throne;


# CONCAT   이 형식대로 문장도 나옴
SELECT CONCAT(Address, " ", PostalCode, " ", City)
		AS Address
FROM Customers;


# CONCAT_WS  맨 앞에 사이에 넣을 문자를 미리 제시
SELECT CONCAT_WS("유후", Address, PostalCode, City) AS Address
FROM customers;

# FIELD
SELECT FIELD("Q", "s", "q", "l");   -- Q가 몇번째에 있냐
SELECT FIELD(5, 0, 1, 2, 3, 4, 5);  -- 5까지 몇개냐

# FIND_IN_SET
SELECT FIND_IN_SET("a", "s,q,l"); --  sql중에 a가 없어서 0
SELECT FIND_IN_SET("q", NULL);    
-- 스트링과 스트링 리스트 중에 null이 있으면 -> null

# FORMAT
SELECT FORMAT(250500.5634, 1);  -- 소수점 몇 번째 자리표시

# INSERT  -- 앞에 숫자로 자리지정 후에 뒤에 숫자는 얼만큼 선 단어를 지울건지
SELECT INSERT("W3Schools.com", 1, 9, "Example");
SELECT INSERT("W3Schoolscom", 4, 2, "noPAD");

# 