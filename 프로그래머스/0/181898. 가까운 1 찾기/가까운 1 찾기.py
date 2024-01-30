def solution(arr, idx):
    answer = 0
    
    """
    idx에 맞춰 arr 자르고(new_arr), 첫 번째 1인 원소 위치 찾아서 idx 길이 더하기
    """
    new_arr = arr[idx:]
    
    if new_arr.count(1) != 0:
        answer = new_arr.index(1)+idx
    else:
        answer = -1
    
    return answer