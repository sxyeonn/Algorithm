def solution(sides):
    answer = 2
    sort_arr = sorted(sides)
    if sort_arr[0] + sort_arr[1] > sort_arr[2]:
        answer = 1
    return answer