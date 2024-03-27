def solution(chicken):
    answer = 0
    coupon = 0
    # tmp는 현재 시킨 치킨 수
    # answer은 모든 서비스 치킨 수(tmp의 합)
    tmp = chicken

    while tmp > 0:
        coupon += tmp % 10
        answer += tmp // 10
        tmp = tmp // 10
    
    # coupon이 10개 이상이면 서비스 치킨 1마리를 시킬 수 있으므로, 
    # 별도의 while문을 두어 처리
    coupon += tmp
    while coupon >= 10:
        # t는 현재 시킨 서비스 치킨 수
        t = coupon // 10
        answer += t
        coupon += t
        coupon -= t * 10

    
    return answer