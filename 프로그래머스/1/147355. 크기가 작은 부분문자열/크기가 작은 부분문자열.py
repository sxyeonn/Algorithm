def solution(t, p):
    answer = 0
    for i in range(len(t)):
        # t에서 p 길이까지 범위를 tmp에 저장
        tmp = t[i:i+len(p)]
        
        # tmp와 p의 길이가 같고, tmp가 p보다 같거나 작으면 answer 증가
        if (len(tmp) == len(p)) & (int(tmp) <= int(p)):
            answer += 1
    return answer