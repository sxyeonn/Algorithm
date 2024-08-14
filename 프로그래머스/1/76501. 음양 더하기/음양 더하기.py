def solution(absolutes, signs):
    answer = 0
    for i in range(len(signs)):
        if signs[i]:   # 참이면
            answer += absolutes[i]
        
        else:   # 거짓이면    
            answer += -absolutes[i]
    
    return answer