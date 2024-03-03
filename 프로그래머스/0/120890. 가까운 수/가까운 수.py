def solution(array, n):
    # 배열의 원소와 n 차이의 값을 담을 배열 diff
    diff = []
    # 주어진 배열을 오름차순 정렬한 배열(sort_arr) (이유: 가까운 수가 여러 개일 경우 더 작은 수를 return 해야함)
    sort_arr = sorted(array)
    for i in sort_arr:
        # diff 배열에 원소와 n의 차이의 절댓값을 담음
        diff.append(abs(i-n))
    # diff 배열의 최솟값의 인덱스를 뽑아, 그 인덱스에 해당하는 sort_arr의 값을 return 함
    return sort_arr[diff.index(min(diff))]