# 약수의 개수를 구하는 함수
def solve_num(num):
    tmp = 0
    for i in range(1, num+1):
        if num / i == int(num / i):
            tmp += 1
    return tmp

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        # 약수의 개수가 짝수이면 수를 더함
        if solve_num(i) % 2 == 0:
            answer += i
        # 약수의 개수가 홀수이면 수를 뺌
        else:
            answer -= i

    return answer