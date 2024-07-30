def solution(n):
    answer = 0
    li = list(str(n))
    li = sorted(li, reverse = True)
    return int(''.join(li))