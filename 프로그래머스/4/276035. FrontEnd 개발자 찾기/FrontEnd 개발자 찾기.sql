/*
- DEVELOPERS 테이블에서 Front End 스킬을 가진 개발자의 정보 조회
- 개발자의 ID, 이메일, 이름, 성을 조회
- ID를 기준으로 오름차순
*/
SELECT DISTINCT d.ID, d.EMAIL, d.FIRST_NAME, d.LAST_NAME
FROM DEVELOPERS d INNER JOIN SKILLCODES s
ON d.SKILL_CODE = d.SKILL_CODE | s.CODE
WHERE s.CATEGORY = 'Front End'
ORDER BY d.ID;