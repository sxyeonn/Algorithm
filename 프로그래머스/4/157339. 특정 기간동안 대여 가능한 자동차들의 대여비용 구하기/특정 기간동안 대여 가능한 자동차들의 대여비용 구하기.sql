/*
- 대여 중인 자동차들의 정보 : CAR_RENTAL_COMPANY_CAR
-> 자동차 ID, 자동차 종류, 일일 대여 요금(원), 자동차 옵션 리스트

- 자동차 대여 기록 정보 : CAR_RENTAL_COMPANY_RENTAL_HISTORY
-> 자동차 대여 기록 ID, 자동차 ID, 대여 시작일, 대여 종료일

- 자동차 종류 별 대여 기간 종류 별 할인 정책 정보 : CAR_RENTAL_COMPANY_DISCOUNT_PLAN
-> 요금 할인 정책 ID, 자동차 종류, 대여 기간 종류, 할인율(%)

<문제>
- 자동차 종류 = '세단' OR 자동차 종류 = 'SUV'
- 2022년 11월 1일부터 2022년 11월 30일까지 대여 가능(END_DATE가 2022-11-01 이전인거 빼고 )
- 30일간의 대여 금액이 50만원 이상, 200만원 미만
- 자동차 ID, 자동차 종류, 대여 금액(FEE) 출력
- 대여 금액 순으로 내림차순, 자동차 종류 순으로 오름차순, 자동차 ID 순으로 내림차순

*/

WITH car_price AS (
    SELECT c.car_id, c.car_type,
        ROUND(c.daily_fee * (1 - (p.discount_rate / 100)) * 30) AS FEE
    FROM CAR_RENTAL_COMPANY_CAR c INNER JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN p
    ON c.CAR_TYPE = p.CAR_TYPE
    WHERE p.duration_type = '30일 이상'
        AND (c.CAR_TYPE = '세단' OR c.CAR_TYPE = 'SUV')
)

SELECT car.CAR_ID AS CAR_ID, car.CAR_TYPE AS CAR_TYPE, car.FEE
FROM car_price car 
    INNER JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY hist
    ON car.CAR_ID = hist.CAR_ID
-- WHERE NOT hist.END_DATE >= '2022-11-01'
WHERE (car.FEE >= 500000 AND car.FEE < 2000000)
GROUP BY car.CAR_ID
HAVING MAX(hist.END_DATE) < '2022-11-01'
ORDER BY car.FEE DESC, car.CAR_TYPE ASC, car.CAR_ID DESC;