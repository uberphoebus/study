select a.고객아이디,
             a.고객이름,
             d.product_name 상품명,
             sum(c.sales) 상품매출,
             rank() over(partition by a.고객아이디 order by sum(c.sales) desc) 선호도순위
      from
      (
        select a.customer_id 고객아이디,
               a.customer_name 고객이름,
               sum(c.sales) 전용상품매출
        from customer a, reservation b, order_info c
        where a.customer_id = b.customer_id
        and   b.reserv_no   = c.reserv_no
        and   b.cancel      = 'N'
        and   c.item_id     = 'M0001'
        group by a.customer_id, a.customer_name
        having sum(c.sales) >= 216000
       ) a, reservation b, order_info c, item d
       group by a.고객아이디, a.고객이름, d.product_name
