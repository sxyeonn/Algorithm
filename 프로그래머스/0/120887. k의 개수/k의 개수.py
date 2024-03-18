def solution(i, j, k):
    answer = 0
    # 첫 시작은 i
    cnt = i
    
    # i부터 j까지 숫자 중..
    while cnt <= j:
        # 각 숫자에 k가 몇 번 등장하는지 셈
        answer += str(cnt).count(str(k))
        cnt += 1
    return answer