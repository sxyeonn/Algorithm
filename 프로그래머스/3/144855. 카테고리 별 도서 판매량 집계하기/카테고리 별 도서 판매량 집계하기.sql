/*
- 2022년 1월의 카테고리 별 도서 판매량
- 카테고리(CATEGORY), 총 판매량(TOTAL_SALES) 리스트 출력
- 카테고리명 기준 오름차순
*/
SELECT b.CATEGORY, SUM(s.SALES) AS TOTAL_SALES
FROM BOOK b INNER JOIN BOOK_SALES s
ON b.BOOK_ID = s.BOOK_ID
WHERE s.SALES_DATE BETWEEN '2022-01-01' AND '2022-01-31'
GROUP BY b.CATEGORY
ORDER BY b.CATEGORY