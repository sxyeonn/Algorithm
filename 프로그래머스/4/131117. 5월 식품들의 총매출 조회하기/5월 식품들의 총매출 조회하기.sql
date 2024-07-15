/*
FOOD_PRODUCT : 식품 ID, 식품 이름, 식품코드, 식품분류, 식품 가격
FOOD_ORDER   : 주문 ID, 제품 ID, 주문량, 생산일자, 입고일자, 출고일자, 공장 ID, 창고 ID
- 생산일자가 2022년 5월인 식품들의 식품 ID, 식품 이름, 총매출을 조회
- 총 매출은 가격 * 판매량
- 총매출을 기준으로 내림차순 정렬, 식품 ID를 기준으로 오름차순 정렬
*/

SELECT p.PRODUCT_ID, 
        p.PRODUCT_NAME, 
        (p.PRICE * SUM(o.AMOUNT)) AS TOTAL_SALES
FROM FOOD_PRODUCT p INNER JOIN FOOD_ORDER o
    ON p.PRODUCT_ID = o.PRODUCT_ID
WHERE o.PRODUCE_DATE LIKE '2022-05%'
GROUP BY p.PRODUCT_NAME
ORDER BY TOTAL_SALES DESC, PRODUCT_ID ASC;
