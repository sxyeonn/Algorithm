def solution(arr):
    # answer의 초기값을 arr의 첫 번째 값으로
    answer = [arr[0]]
    for i in range(len(arr)):
        # arr 원소와 answer의 직전 값이 같지 않으면 arr 원소 삽입
        if arr[i] != answer[-1]:
            answer.append(arr[i])
    return answer