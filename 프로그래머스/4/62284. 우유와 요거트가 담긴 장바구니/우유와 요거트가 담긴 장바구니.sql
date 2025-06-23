SELECT CART_ID
FROM CART_PRODUCTS
-- Milk or Yogurt 구매 이력
WHERE NAME = 'Milk' OR NAME = 'Yogurt'
GROUP BY CART_ID
-- 장바구니 ID로 그룹핑함과 동시에 중복되지 않은 상품 종류가 2가지인 것만 가져옴
-- 상품 종류를 where 절로 milk와 yogurt로 한정했기 때문에 중복되지 않은 상품 종류가 2가지인 장바구니는
-- 두 상품을 동시에 구입한 장바구니임.
HAVING COUNT(DISTINCT NAME) = 2
ORDER BY CART_ID;