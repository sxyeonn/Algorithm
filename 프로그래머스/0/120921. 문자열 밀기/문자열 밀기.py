def solution(A, B):
    answer = -1
    
    ## 처음부터 A와 B가 같으면 for문을 돌지 않음
    if A==B:
        return 0
        
    for i in range(1, len(A)) :
        ## A를 오른쪽으로 한 칸씩 밀어보며, B와 같은지 비교한다. 
        # A[-1]은 A의 마지막 문자열을 의미하고, A[0:-1]은 0인덱스부터 마지막 문자열 전까지의 문자열을 의미
        A = A[-1] + A[0:-1]

        if A == B:
            return i  
            
    return answer