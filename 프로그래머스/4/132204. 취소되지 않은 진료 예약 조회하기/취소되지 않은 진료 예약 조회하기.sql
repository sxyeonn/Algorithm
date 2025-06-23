-- 2022년 4월 13일 취소되지 않은 흉부외과(CS) 진료 예약 내역
-- 진료예약번호(a), 환자이름(p), 환자번호(p), 진료과코드(a), 의사이름(d), 진료예약일시(a) 출력
-- 진료예약일시를 기준으로 오름차순

SELECT a.APNT_NO, p.PT_NAME, p.PT_NO, a.MCDP_CD
        , d.DR_NAME, a.APNT_YMD
FROM APPOINTMENT a JOIN PATIENT p ON a.PT_NO = p.PT_NO
                   JOIN DOCTOR d ON a.MDDR_ID = d.DR_ID
WHERE a.MCDP_CD = 'CS'
    AND DATE_FORMAT(a.APNT_YMD, '%Y-%m-%d') = '2022-04-13'
    AND APNT_CNCL_YMD IS NULL
ORDER BY a.APNT_YMD