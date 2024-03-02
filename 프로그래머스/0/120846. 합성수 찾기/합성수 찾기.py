def solution(n):
    # 1과 2는 합성수X, 2를 제외한 모든 짝수는 합성수
    answer = 0
    for i in range(n):
        if (i+1) != 2 and (i+1) % 2 == 0:
            # i+1이 2가 아닌 모든 짝수일 경우 answer을 +1 한다. 
            answer += 1
            
        elif (i+1) != 1 and (i+1) % 2 != 0:
            # i+1이 1이 아닌 모든 홀수를 체크한다. 
            measure = 0 # 각 숫자의 약수를 담을 measure
            for j in range(i):  # 각 숫자보다 작은 수들을 순회하며..
                if (i+1)/(j+1) == int((i+1)/(j+1)):
                # 값을 나눈 것이 소숫점없이 떨어지는 수(약수)이면 measure을 증가시킨다. 
                    measure += 1
                    # 약수의 개수가 2개가 이상이면(자기자신도 약수이므로 이는 제외한다) 
                    # 합성수로 판단하여 answer을 하나 증가시키고, for문을 멈춘다. 
                    if measure >= 2:
                        answer += 1
                        break
    return answer