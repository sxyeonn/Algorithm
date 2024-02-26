def solution(emergency):
    answer = []
    sort_arr = sorted(emergency, reverse=True)
    for i in range(len(emergency)):
        answer.append(sort_arr.index(emergency[i]) + 1)
    
    return answer