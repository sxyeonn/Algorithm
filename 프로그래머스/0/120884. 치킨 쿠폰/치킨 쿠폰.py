def solution(chicken):
    answer = 0
    coupon = 0
    # tmp는 현재 시킨 치킨 수
    # answer은 모든 서비스 치킨 수(tmp의 합)
    tmp = chicken

    while tmp > 0:
        print("현재 시킨 치킨 수(tmp), 쿠폰 수, answer : ", tmp, coupon, answer)
        coupon += tmp % 10
        answer += tmp // 10
        tmp = tmp // 10
    
    coupon += tmp
    print(coupon, answer)
    while coupon >= 10:
    #if coupon >= 10:
        t = coupon // 10
        answer += t
        coupon += t
        coupon -= t * 10
    print(coupon, answer)

    
    """
    print("--------")
    tmp = tmp // 10
    coupon += tmp % 10
    answer += tmp // 10
    print("현재 시킨 수(tmp), 쿠폰 수, answer : ", tmp, coupon, answer)
    
    
    print("--------")
    tmp = tmp // 10
    coupon += tmp % 10
    answer += tmp // 10
    print("현재 시킨 수(tmp), 쿠폰 수, answer : ", tmp, coupon, answer)
    
    print("--------")
    tmp = tmp // 10
    coupon += tmp % 10
    answer += tmp // 10
    print("현재 시킨 수(tmp), 쿠폰 수, answer : ", tmp, coupon, answer)
    
    print("--------")
    tmp = tmp // 10
    coupon += tmp % 10
    answer += tmp // 10
    print("현재 시킨 수(tmp), 쿠폰 수, answer : ", tmp, coupon, answer)
    """
    
    
    return answer