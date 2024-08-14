def solution(num):
    answer = 0
    
    while num != 1:
        if num % 2 == 0:        # 짝수라면
            num = num / 2

        else:                   # 홀수라면
            num = num * 3 + 1

        answer += 1
        
        # 작업을 500번 반복할 때까지 1이 되지 않는다면
        if answer == 500:
            answer = -1
            break
            
    return answer