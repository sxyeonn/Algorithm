def solution(spell, dic):

    new_arr = []
    # spell의 원소가 전부 한 번씩 사용되어야함
    # spell의 원소 중 하나라도 dic의 각 원소에 없으면 break. 
    # spell의 원소를 갖고 있는 dic을 new_arr에 추가
    for d in dic:
        for s in spell:
            if s not in d:
                break
            new_arr.append(d)
            
    # new_arr에는 spell의 각 원소를 포함하는 dic원소가 모두 들어가있음
    for i in new_arr:
        if new_arr.count(i) == len(spell):
            return 1
            
    return 2