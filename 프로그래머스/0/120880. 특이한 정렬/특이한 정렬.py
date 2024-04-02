def solution(numlist, n):
    # 거리가 n에 가까운 순으로 정렬, 절댓값이 같으면 양수(= 큰 값) 먼저
    answer = sorted(numlist,key = lambda x : (abs(x-n), n-x))
    return answer
