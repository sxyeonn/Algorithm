from fractions import Fraction
import math

def solution(a, b):
    # 기약분수 만들기
    f = Fraction(a, b)
    # 기약분수의 분모 값을 check_num에 담음
    check_num = f.denominator
    # 소인수분해
    # 나누는 수 d
    d = 2
    # 소인수를 담을 리스트 f_list
    f_list = []

    while d <= check_num:
        if check_num % d == 0:
            if d not in f_list:
                f_list.append(d)
            check_num = check_num / d
        else:
            d = d + 1
    
    # 소인수 중 2나 5가 있으면 제거
    # 제거 후 아무것도 남아있지 않으면 return 1
    if 2 in f_list:
        f_list.remove(2)
    if 5 in f_list:
        f_list.remove(5)
    if len(f_list) == 0:
        return 1
    return 2