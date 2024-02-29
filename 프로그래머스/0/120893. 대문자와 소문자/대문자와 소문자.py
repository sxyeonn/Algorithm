def solution(my_string):
    answer = ''
    
    for i in my_string:
        # i가 대문자면 소문자로 변경하여 answer에 추가
        if i == i.upper():
            answer += i.lower()
        # i가 소문자면 대문자로 변경하여 answer에 추가
        else:
            answer += i.upper()
    return answer