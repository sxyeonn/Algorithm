-- 더 이상 업그레이드할 수 없는 아이템 조회
-- 아이템 ID(ITEM_ID), 아이템 명(ITEM_NAME), 아이템의 희귀도(RARITY)를 출력
-- 아이템 ID를 기준으로 내림차순
/*
ITEM_A <- X
ITEM_B <- ITEM_A
ITEM_C <- ITEM_A
ITEM_D <- ITEM_B
ITEM_E <- ITEM_B

=> 즉, ITEM_A와 ITEM_B은 무언가로 업그레이드가 가능하나, 다른 아이템들은 불가함
==> 정리하자면, 'PARENT_ITEM_ID'에 없는 ITEM_ID를 구하면 되는 것이다!

*/
SELECT i.ITEM_ID, i.ITEM_NAME, i.RARITY
FROM ITEM_INFO i JOIN ITEM_TREE t
ON i.ITEM_ID = t.ITEM_ID
WHERE i.ITEM_ID NOT IN (
            SELECT PARENT_ITEM_ID
            FROM ITEM_TREE
            WHERE PARENT_ITEM_ID IS NOT NULL
)
ORDER BY i.ITEM_ID DESC;
