def solution(s):
    count_p = s.count('p') + s.count('P')
    count_y = s.count('y') + s.count('Y')
    return False if count_p != count_y else True