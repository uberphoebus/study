
/* 모두의 SQL 12장 실습 */

# 분석1
-- 전체 상품의 주문 완료건의
-- 총 매출, 평균 매출, 최고 매출, 최저 매출 출력

-- 모범답안
SELECT COUNT(*) 전체주문건,
		SUM(b.sales) 총매출,
		AVG(b.sales) 평균매출,
		MAX(b.sales) 최고매출,
		MIN(b.sales) 최저매출
	FROM reservation a, order_info b
	WHERE a.reserv_no = b.reserv_no;


# 분석2
-- 전체 상품의 총 판매량과 총 매출액,
-- 전용 상품의 판매량과 매출액 출력
-- item_id = 'm0001'

-- 내 답안
SELECT SUM(quantity),
		SUM(quantity * sales)
		FROM order_info;

-- 모범답안
SELECT COUNT(*) 총판매량,
		 SUM(b.sales) 총매출,
		 SUM(case b.item_id
		 			when 'M0001' then 1
		 			ELSE 0
		 		END) 전용상품판매량,
		 SUM(case b.item_id
		 			when 'M0001' then b.sales
		 			ELSE 0
		 		END) 전용상품매출액
	FROM order_info b;


# 분석3
-- 각 상품별 전체 매출액 내림차순

-- 모범답안
SELECT b.item_id 상품코드, 
		 c.product_name 상품이름, 
		 SUM(b.sales) 상품매출
FROM reservation a, order_info b, item c
WHERE a.reserv_no = b.reserv_no
		AND a.cancel = 'N'
		AND b.item_id = c.item_id
GROUP BY b.item_id, c.product_name
ORDER BY SUM(b.sales) DESC;


# 분석4; 오라클 decode는 case로 변환
-- 모든 상품의 월별 매출액 출력

-- 모범답안
SELECT SUBSTR(a.reserv_date, 1, 6) 매출년월,
		 SUM( case b.item_id when 'M0001' then b.sales
		 			ELSE 0 END ) SPECial_SET,
		 SUM( case b.item_id when 'M0002' then b.sales
		 			ELSE 0 END ) PASTA,
		 SUM( case b.item_id when 'M0003' then b.sales
		 			ELSE 0 END ) PIZZA,
		 SUM( case b.item_id when 'M0004' then b.sales
		 			ELSE 0 END ) SEA_FOOD,
		 SUM( case b.item_id when 'M0005' then b.sales
		 			ELSE 0 END ) STEAK,
		 SUM( case b.item_id when 'M0006' then b.sales
		 			ELSE 0 END ) SALAD_BAR,
		 SUM( case b.item_id when 'M0007' then b.sales
		 			ELSE 0 END ) SALAD,
		 SUM( case b.item_id when 'M0008' then b.sales
		 			ELSE 0 END ) SANDWICH,
		 SUM( case b.item_id when 'M0009' then b.sales
		 			ELSE 0 END ) WINE,
		 SUM( case b.item_id when 'M0010' then b.sales
		 			ELSE 0 END ) JUICE
 FROM reservation a, order_info b
WHERE a.reserv_no = b.reserv_no 
		AND a.cancel = 'N'
GROUP BY SUBSTR(a.reserv_date, 1, 6)
ORDER BY SUBSTR(a.reserv_date, 1, 6);


# 분석5
-- 월별 총 매출액과 전용 상품 매출액을 출력

-- 내 답안
SELECT SUBSTR(a.reserv_date, 1, 6) 매출년월,
		 SUM(b.sales) 총매출,
		 SUM( case b.item_id when 'M0001' then b.sales 
		 			ELSE 0 END ) 전용상품매출액
 FROM reservation a, order_info b
WHERE a.reserv_no = b.reserv_no 
		AND a.cancel = 'N'
GROUP BY SUBSTR(a.reserv_date, 1, 6)
ORDER BY SUBSTR(a.reserv_date, 1, 6);


# 분석6
-- 분석5에 매출 기여율 추가
-- 기겨율은 소수점 아래 두 번재 자리에서 반올림

-- 내 답안
SELECT SUBSTR(a.reserv_date, 1, 6) 매출년월,
		 ( SUM(b.sales)
		 		- SUM( case b.item_id when 'M0001' then b.sales 
				 			ELSE 0 END ) ) 전용상품외매출,
		 SUM( case b.item_id when 'M0001' then b.sales 
		 			ELSE 0 END ) 전용상품매출,
		 ROUND( SUM( case b.item_id when 'M0001' then b.sales 
		 					ELSE 0 END )
		 					/ SUM(b.sales) * 100, 1 ) 매출기여도
 FROM reservation a, order_info b
WHERE a.reserv_no = b.reserv_no 
		AND a.cancel = 'N'
GROUP BY SUBSTR(a.reserv_date, 1, 6)
ORDER BY SUBSTR(a.reserv_date, 1, 6);



##################################################

SELECT * FROM address;
SELECT * FROM customer;
SELECT * FROM item;
SELECT * FROM order_info;
SELECT * FROM reservation;



