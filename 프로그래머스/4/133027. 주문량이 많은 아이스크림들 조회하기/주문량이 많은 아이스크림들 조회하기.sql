/*
FIRST_HALF : 아이스크림 공장에서 아이스크림 가게까지의 출하 번호, 아이스크림 맛, 상반기 아이스크림 총주문량
JULY       : 아이스크림 공장에서 아이스크림 가게까지의 출하 번호, 아이스크림 맛, 7월 아이스크림 총주문량

- 7월 아이스크림 총 주문량과 상반기의 아이스크림 총 주문량을 더한 값이 큰 순서대로 상위 3개의 맛을 조회
*/
SELECT j.FLAVOR
FROM JULY j LEFT JOIN FIRST_HALF f
    ON j.SHIPMENT_ID = f.SHIPMENT_ID
GROUP BY j.FLAVOR
ORDER BY SUM(j.TOTAL_ORDER) + SUM(f.TOTAL_ORDER) DESC
LIMIT 3;