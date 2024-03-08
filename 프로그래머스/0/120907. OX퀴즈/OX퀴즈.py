# 수식이 옳은지 판단하는 함수
def exp(numbers):
    # 공백을 기준으로 식을 나눔
    expression = numbers.split(" ")
    if expression[1] == "+":
        tmp = int(expression[0]) + int(expression[2])
    else:
        tmp = int(expression[0]) - int(expression[2])
    
    if tmp == int(expression[-1]):
        return "O"
    else:
        return "X"
    
def solution(quiz):
    answer = []
    for i in quiz:
        # 수식을 계산하는 함수를 수식마다 적용하여 answer을 구함
        answer.append(exp(i))
    return answer