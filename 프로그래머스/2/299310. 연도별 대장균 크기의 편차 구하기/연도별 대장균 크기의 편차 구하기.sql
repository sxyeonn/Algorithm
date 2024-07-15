/*
- 분화된 연도(YEAR)
- 분화된 연도별 대장균 크기의 편차(YEAR_DEV) = 분화된 연도별 가장 큰 대장균의 크기 - 각 대장균의 크기
- 대장균 개체의 ID(ID)
- YEAR에 대해 오름차순, YEAR_DEV에 대해 오름차순
*/
WITH yearMax AS (
    SELECT YEAR(DIFFERENTIATION_DATE) AS YEAR, 
           MAX(SIZE_OF_COLONY) AS Max_Size
    FROM ECOLI_DATA
    GROUP BY YEAR(DIFFERENTIATION_DATE)
)

SELECT 
    yearMax.YEAR,
    (yearMax.Max_Size - ECOLI_DATA.SIZE_OF_COLONY) AS YEAR_DEV, 
    ECOLI_DATA.ID
FROM ECOLI_DATA
INNER JOIN yearMax
ON YEAR(ECOLI_DATA.DIFFERENTIATION_DATE) = yearMax.YEAR
ORDER BY YEAR ASC, YEAR_DEV ASC;
