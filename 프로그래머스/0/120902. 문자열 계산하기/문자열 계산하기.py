def solution(my_string):
    # 공백을 기준으로 문자열을 나눈다. 
    new_str = my_string.split(' ')
    # 정확한 수식은 첫 번째로 연산자가 나오지 않으므로 기본 answer은 첫 번째 숫자로 지정한다. 
    answer = int(new_str[0])
    for i in range(len(new_str)):
        # + 연산자를 만나면, 지금까지의 answer과 연산자 바로 뒤에 올 값을 더한다. 
        if new_str[i] == "+":
            answer = answer + int(new_str[i+1])
        # - 연산자를 만나면, 지금까지의 answer과 연산자 바로 뒤에 올 값을 뺀다. 
        elif new_str[i] == "-":
            answer = answer - int(new_str[i+1])
    return answer