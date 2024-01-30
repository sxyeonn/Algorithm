def solution(my_string):
    answer = []
    
    for alphabet in 'abcdefghijklmnopqrstuvwxyz'.upper():
        answer.append(my_string.count(alphabet))
    
    for alphabet in 'abcdefghijklmnopqrstuvwxyz':
        answer.append(my_string.count(alphabet))
        
    
    return answer