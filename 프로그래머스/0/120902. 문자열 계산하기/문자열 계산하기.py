def solution(my_string):
    new_str = my_string.split(' ')
    answer = int(new_str[0])
    for i in range(len(new_str)):
        tmp = 0
        if new_str[i] == "+":
            answer = answer + int(new_str[i+1])
        elif new_str[i] == "-":
            answer = answer - int(new_str[i+1])
    return answer