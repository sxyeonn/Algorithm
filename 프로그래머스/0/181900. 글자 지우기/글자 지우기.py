def solution(my_string, indices):
    answer = ''
    
    for s in range(len(my_string)):
        if s not in indices:
            answer += my_string[s]
    
    return answer