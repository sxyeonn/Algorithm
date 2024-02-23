import math
def solution(slice, n):
    answer = 0
    
    # n명이 최소 1조각 이상 먹음 => slice * answer
    print(math.ceil(n/slice))
    """
    if n%slice == 0:
        answer = n/slice
    else:
        answer = n//slice + 1
    """
    return math.ceil(n/slice)