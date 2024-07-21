/*
- ANIMAL_INS : 보호소에 들어온 동물의 정보를 담은 테이블
- ANIMAL_OUTS : 입양 보낸 동물의 정보를 담은 테이블
<조건>
- 보호소에 들어올 당시에는 중성화되지 않았지만(Intact),
- 보호소를 나갈 당시에는 중성화된 동물 찾기
- 동물의 아이디, 생물종, 이름 조회 (아이디 순 정렬)
*/
-- 보호소에 들어올 당시 중성화되지 않았던 동물 찾기
SELECT i.ANIMAL_ID, i.ANIMAL_TYPE, i.NAME
FROM ANIMAL_INS i INNER JOIN ANIMAL_OUTS o
ON i.ANIMAL_ID = o.ANIMAL_ID
WHERE i.SEX_UPON_INTAKE LIKE '%Intact%'
    AND (o.SEX_UPON_OUTCOME LIKE '%Spayed%' OR o.SEX_UPON_OUTCOME LIKE '%Neutered%')
ORDER BY i.ANIMAL_ID