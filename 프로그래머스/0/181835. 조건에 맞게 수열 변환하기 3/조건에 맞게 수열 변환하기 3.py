def solution(arr, k):
    if k%2 != 0:
        arr = list(map(lambda x:x*k, arr))
    else:
        arr = list(map(lambda x:x+k, arr))
    return arr

    # return list(map(lambda x:x+k, arr)) if k%2 else list(map(lambda x:x*k, arr))