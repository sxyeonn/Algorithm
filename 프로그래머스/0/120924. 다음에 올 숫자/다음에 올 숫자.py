def solution(common):
    answer = 0
    if common[1] - common[0] == common[2] - common[1]:
        # 원소 (1-0) = (2-1)이면 등차수열
        answer = common[-1] + (common[1] - common[0])
    else:
        # 등비수열
        answer = common[-1] * (common[1] // common[0])
    return answer