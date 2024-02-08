def solution(arr, k):
    # answer = list(set(arr))
    answer = [i for n, i in enumerate(arr) if i not in arr[:n]]
    if len(answer) >= k:
        answer = answer[:k]
    else:
        for x in range(k-len(answer)):
            answer.append(-1)
    return answer