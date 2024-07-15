/*
- 물고기 종류 별로 가장 큰 물고기의 ID, 물고기 이름, 길이를 출력
- 물고기의 ID 컬럼명은 ID, 이름 컬럼명은 FISH_NAME, 길이 컬럼명은 LENGTH
- 물고기의 ID에 대해 오름차순
- 물고기 종류별 가장 큰 물고기는 1마리만 있으며 10cm 이하의 물고기가 가장 큰 경우는 없다.
*/
SELECT info.ID as ID,
       name.FISH_NAME as FISH_NAME, 
       info.LENGTH as LENGTH
FROM FISH_INFO info 
INNER JOIN FISH_NAME_INFO name ON info.FISH_TYPE = name.FISH_TYPE
WHERE (info.FISH_TYPE, info.LENGTH) IN (
                                        SELECT FISH_TYPE, MAX(LENGTH)
                                        FROM FISH_INFO
                                        GROUP BY FISH_TYPE)
ORDER BY info.ID;                                        