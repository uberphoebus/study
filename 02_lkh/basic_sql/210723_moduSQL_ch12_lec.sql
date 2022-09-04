-------------------------------------------
분석1) 전체 상품의 주문 완료 건 총 매출,
평균 매출, 최고매출, 최저 매출을
출력해 보세요. 
--------------------------------------------

SELECT COUNT(*) 주문완료건,
       SUM(b.sales) 총매출,
       AVG(b.sales) 평균매출,
       MAX(b.sales) 최고매출,
       MIN(b.sales) 최저매출       
  FROM reservation a, order_info b
  WHERE a.reserv_no = b.reserv_no;

# 주문완료건 391, 총매출 24,957,000
#  평균매출 63,828 최고 552,000  최저 6,000


----------------------------------------------
분석2) 전체 상품의 총 판매량과 총 매출액, 
전용 상품의 판매량과 매출액을 출력
item_id = "M0001"
----------------------------------------------

SELECT COUNT(*) 총판매량,
       SUM(b.sales) 총매출, 
       SUM(case b.item_id when 'M0001' 
		          then 1 ELSE 0 
			  END) 전용상품판매,
       SUM(case b.item_id when 'M0001' 
		          then b.sales ELSE 0 
				END) 전용상품매출 
FROM reservation a, order_info b
WHERE a.reserv_no = b.reserv_no 
  AND a.cancel = 'N'; 
  
# 총판매량 391, 총매출 24,957,000
#   전용상품판매 59, 총매출 5,808,000
 
SELECT COUNT(sales)
  FROM order_info
WHERE item_id = 'M0001';

SELECT sum(sales)
  FROM order_info
WHERE item_id = 'M0001';
  
  
-------------------------------------------------
분석3) 각 상품별 전체 매출액을 내림차순으로 출력
-------------------------------------------------

SELECT b.item_id 상품코드,
       c.product_name 상품이름,
       sum(b.sales) 상품매출
FROM reservation a, order_info b, item c
WHERE a.reserv_no = b.reserv_no 
  AND a.cancel = 'N'
  AND b.item_id = c.item_id
GROUP BY b.item_id, c.product_name
ORDER BY SUM(b.sales) desc; 
  
-----------------------------------------
분석4) 모든 상품의 월별 매출액을 출력
-----------------------------------------
SELECT SUBSTR(a.reserv_date, 1,6) 매출년월,
       SUM(case b.item_id when "M0001" then b.sales 
		          ELSE 0 END) SPECIAL_SET,
       SUM(case b.item_id when "M0002" then b.sales 
		          ELSE 0 END) PASTA,
       SUM(case b.item_id when "M0003" then b.sales 
		          ELSE 0 END) PIZZA,
       SUM(case b.item_id when "M0004" then b.sales 
		          ELSE 0 END) SEA_FOOD,
       SUM(case b.item_id when "M0005" then b.sales 
		          ELSE 0 END) STEAK,
       SUM(case b.item_id when "M0006" then b.sales 
		          ELSE 0 END) SALAD_BAR,
       SUM(case b.item_id when "M0007" then b.sales 
		          ELSE 0 END) SALAD,
       SUM(case b.item_id when "M0008" then b.sales 
		          ELSE 0 END) SANDWICH,
       SUM(case b.item_id when "M0009" then b.sales 
		          ELSE 0 END) WINE,
       SUM(case b.item_id when "M0010" then b.sales 
		          ELSE 0 END) JUICE
 FROM reservation a, order_info b
WHERE a.reserv_no = b.reserv_no 
  AND a.cancel = 'N'
GROUP BY SUBSTR(a.reserv_date, 1,6)
ORDER BY SUBSTR(a.reserv_date, 1,6); 

------------------------------------------------
분석5) 월별 총 매출액과 전용 상품 매출액을 출력 
------------------------------------------------
SELECT SUBSTR(a.reserv_date,1,6) 매출월,
       SUM(b.sales) 총매출,
       SUM(case b.item_id when 'M0001' then b.sales 
		          ELSE 0 END) 전용상품매출
FROM reservation a, order_info b
WHERE a.reserv_no = b.reserv_no
  AND a.cancel = 'N'
GROUP BY SUBSTR(a.reserv_date, 1,6)
ORDER BY SUBSTR(a.reserv_date, 1,6); 

----------------------------------------------------------
분석6) 분석5에 매출 기여율을 추가하세요. 
       기여율은  소수점 아래 두 번째 자리에서 반올림 출력
----------------------------------------------------------
SELECT SUBSTR(a.reserv_date,1,6) 매출월,
       ( SUM(b.sales)  
         - SUM(case b.item_id when 'M0001' then b.sales 
		          ELSE 0 END)) 전용상품외매출,
       SUM(case b.item_id when 'M0001' then b.sales 
		          ELSE 0 END)  전용상품매,
		 round(SUM(case b.item_id when 'M0001' then b.sales 
		          ELSE 0 END) /
		       SUM(b.sales) * 100,1) 매출기여율
FROM reservation a, order_info b
WHERE a.reserv_no = b.reserv_no
  AND a.cancel = 'N'
GROUP BY SUBSTR(a.reserv_date, 1,6)
ORDER BY SUBSTR(a.reserv_date, 1,6);
 