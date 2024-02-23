def solution(n):
    
    if n%6 == 0:
        return n//6
    else:
        for i in range(6):
            if (n * (i+1)) % 6 == 0:
                return  n * (i+1) // 6
