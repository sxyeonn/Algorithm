def solution(arr):
    answer = [-1]
    if 2 in arr:
        start = arr.index(2)

        for i in range(len(arr), 0, -1):
            if arr[i-1] == 2:
                end = i-1
                break
        
        answer = arr[start:end+1]

    return answer