/*
- USER_INFO : 의류 쇼핑몰에 가입한 회원 정보를 담은 테이블
- ONLINE_SALE : 온라인 상품 판매 정보를 담은 테이블

<조건>
- 2021년에 가입한 회원
- 2021년에 가입한 회원 중 상품을 구매한 회원수 / 2021년에 가입한 전체 회원 수
- 위를 년, 월 별로 출력
- 비율은 소수 첫 번째 자리까지 출력, 년 기준 오름차순, 월 기준 오름차순
*/

-- 2021년에 가입하고 구매한 회원 구하기
WITH join_buy_2021 AS (
    SELECT o.online_sale_id, o.user_id, o.product_id, o.sales_amount, o.sales_date
    FROM ONLINE_SALE o INNER JOIN USER_INFO i
    ON o.USER_ID = i.USER_ID
    WHERE i.JOINED LIKE '2021%'
)
SELECT Year(sales_date) AS YEAR
        , Month(sales_date) AS MONTH
        , count(distinct user_id) AS PURCHASED_USERS
        , ROUND((count(distinct user_id) / (select count(*) from USER_INFO WHERE JOINED LIKE '2021%')), 1) AS PUCHASED_RATIO
FROM join_buy_2021
GROUP BY Year(sales_date), Month(sales_date)
ORDER BY Year(sales_date), Month(sales_date)



