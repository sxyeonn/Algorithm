def solution(n):
    answer = ''
    # n이 짝수면
    if n%2 == 0:
        answer = '수박'*(n//2)
        
    # n이 홀수면
    else:
        answer = '수박'*(n//2) + '수'
        
    return answer