def solution(arr, n):
    if len(arr) % 2 == 0:   # arr 길이가 짝수
        for i in range(1, len(arr), 2):
            arr[i] += n
    else:                   # arr 길이가 홀수
        for i in range(0, len(arr), 2):
            arr[i] += n
    return arr