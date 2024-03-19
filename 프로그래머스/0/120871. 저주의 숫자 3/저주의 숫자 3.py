def solution(n):

    cnt = 0
    # new_num 리스트에 3x 마을에서 사용하는 숫자들을 담음
    new_num = []
    # 10진법 숫자는 100까지 사용되므로, 3x 마을에서 사용하는 숫자 개수도 100개 담음
    while len(new_num) < 100:
        cnt += 1
        # 숫자에 3이 포함되지 않거나 3의 배수가 아닐때..
        if '3' not in str(cnt) and cnt%3 != 0:
            new_num.append(cnt)

    return new_num[n-1]




