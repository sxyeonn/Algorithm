def solution(num_list):
    answer = 0
    for i in num_list:
        while i != 1:
            if i%2 == 0:    # 짝수라면
                i = i/2
            else:
                i = (i-1)/2 # 홀수라면
            answer += 1
    return answer