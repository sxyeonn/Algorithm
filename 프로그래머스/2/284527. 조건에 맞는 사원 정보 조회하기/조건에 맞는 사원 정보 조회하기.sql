/*
- 2022년도 한해 평가 점수(상, 하반기 점수의 합)가 가장 높은 사원 정보
- 사원의 점수, 사번, 성명, 직책, 이메일을 조회
*/
SELECT SUM(g.SCORE) AS SCORE, g.EMP_NO, e.EMP_NAME, e.POSITION, e.EMAIL
FROM HR_EMPLOYEES e INNER JOIN HR_GRADE g
ON e.EMP_NO = g.EMP_NO
GROUP BY g.EMP_NO
ORDER BY SUM(g.SCORE) DESC
LIMIT 1;
