SELECT t.ID
        , CASE WHEN t.ranking <= 25 THEN 'CRITICAL'
               WHEN t.ranking > 25 AND t.ranking <= 50 THEN 'HIGH'
               WHEN t.ranking > 50 AND t.ranking <= 75 THEN 'MEDIUM'
               WHEN t.ranking > 75 AND t.ranking <= 100 THEN 'LOW'
            END AS COLONY_NAME
FROM (
    SELECT ID, SIZE_OF_COLONY
            , (
                (RANK() OVER(ORDER BY SIZE_OF_COLONY DESC))
              / (SELECT COUNT(*) FROM ECOLI_DATA) * 100
              ) AS ranking
    FROM ECOLI_DATA
) t
ORDER BY t.ID;