def solution(my_string):
    answer = 0
    answer += my_string.count('1') * 1
    answer += my_string.count('2') * 2
    answer += my_string.count('3') * 3
    answer += my_string.count('4') * 4
    answer += my_string.count('5') * 5
    answer += my_string.count('6') * 6
    answer += my_string.count('7') * 7
    answer += my_string.count('8') * 8
    answer += my_string.count('9') * 9
    
    return answer