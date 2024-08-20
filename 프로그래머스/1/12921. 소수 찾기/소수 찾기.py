def solution(n):
    answer = 0
    # 1은 소수가 아니기 때문에 2부터 순회하며 소수인 수를 찾음
    for i in range(2, n+1):
        # 소수는 1과 자신으로만 나누어지는 수이므로, 
        # 2 ~ (자기자신-1) 까지의 숫자 중 나누어지는 수가 있으면 소수가 아님
        for j in range(2, (int(i**(0.5)) + 1)):
            if i % j == 0:    
                break
        # 소수가 아니면 answer + 1
        else:
            answer += 1
    return answer