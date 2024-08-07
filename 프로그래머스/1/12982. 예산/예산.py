# 그리디 알고리즘 -> 가장 좋은 것 고르기!
def solution(d, budget):
    answer = 0
    tmp = 0
    # 주어진 금액을 정렬하여, 작은 값부터 차례대로 더함
    for i in sorted(d):
        tmp += i
        # 더한 값이 예산보다 작으면 answer += 1
        if tmp <= budget:
            answer += 1
        else:
            break
    return answer