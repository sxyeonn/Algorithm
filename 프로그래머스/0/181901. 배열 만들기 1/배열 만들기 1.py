def solution(n, k):
    answer = []
    
    for num in range(n):
        if (num+1) % k == 0:
            answer.append(num+1)
            
    
    return answer