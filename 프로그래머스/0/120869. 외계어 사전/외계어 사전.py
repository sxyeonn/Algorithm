def solution(spell, dic):
    answer = 2
    new_arr = []
    # spell의 원소가 전부 한 번씩 사용되어야함
    for d in dic:
        for s in spell:
            if s not in d:
                break
            new_arr.append(d)
    #print(new_arr)
    for i in new_arr:
        if new_arr.count(i) == len(spell):
            return 1
            
    return answer