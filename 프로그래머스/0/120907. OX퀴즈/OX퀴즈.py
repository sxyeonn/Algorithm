# 수식이 옳은지 판단하는 함수
def exp(numbers):
    # 공백을 기준으로 식을 나눔
    expression = numbers.split(" ")
    # 주어진 수식은 일정한 형태를 보이므로, 연산자는 1번 인덱스에 위치하며, 계산할 값은 각각 0번, 2번 인덱스에 위치함. 
    if expression[1] == "+":
        tmp = int(expression[0]) + int(expression[2])
    else:
        tmp = int(expression[0]) - int(expression[2])
    
    # 계산한 수식 값이 결과값(수식의 마지막 값)과 일치하면 O, 불일치하면 X 반환
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