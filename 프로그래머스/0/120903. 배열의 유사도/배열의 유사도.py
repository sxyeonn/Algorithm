def solution(s1, s2):
    answer = 0
    set_list = list(set(s1 + s2))
    print(set_list)
    print(len(set_list), len(s1), len(s2))
    if len(set_list) != len(s1) + len(s2):
        answer = len(s1) + len(s2) - len(set_list)
    return answer