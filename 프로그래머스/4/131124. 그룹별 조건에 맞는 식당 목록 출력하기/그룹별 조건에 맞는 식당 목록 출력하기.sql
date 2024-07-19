/*
- 리뷰를 가장 많이 작성한 회원의 리뷰 조회
- 회원 이름, 리뷰 텍스트, 리뷰 작성일이 출력
- 리뷰 작성일을 기준으로 오름차순, 리뷰 텍스트를 기준으로 오름차순
*/
-- 고객별 리뷰의 개수를 찾는 쿼리
WITH find_reviews AS (
    SELECT MEMBER_ID, REVIEW_TEXT, REVIEW_DATE, count(*) as cnt
    FROM REST_REVIEW
    GROUP BY MEMBER_ID
), 
-- 리뷰를 가장 많이 작성한 회원의 정보를 찾는 쿼리
find_member AS (
    SELECT MEMBER_ID, REVIEW_TEXT, REVIEW_DATE
    FROM find_reviews
    WHERE cnt IN (SELECT max(cnt) FROM find_reviews)
), 
find_member_info AS (
    SELECT MEMBER_ID, REVIEW_TEXT, REVIEW_DATE
    FROM REST_REVIEW
    WHERE MEMBER_ID IN (SELECT MEMBER_ID FROM find_member)
)

SELECT p.MEMBER_NAME
        , f.REVIEW_TEXT
        , DATE_FORMAT(f.REVIEW_DATE, '%Y-%m-%d') AS REVIEW_DATE
FROM find_member_info f 
INNER JOIN MEMBER_PROFILE p
ON f.MEMBER_ID = p.MEMBER_ID
ORDER BY f.REVIEW_DATE, f.REVIEW_TEXT