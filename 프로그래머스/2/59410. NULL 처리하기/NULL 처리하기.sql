-- 동물의 생물 종, 이름, 성별 및 중성화 여부를 아이디 순으로 조회
-- NULL은 "No name"으로
SELECT ANIMAL_TYPE, 
        CASE WHEN NAME IS NULL THEN "No name"
            ELSE NAME
        END AS NAME, 
        SEX_UPON_INTAKE
FROM ANIMAL_INS;