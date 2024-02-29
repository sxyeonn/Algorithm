def solution(num_list, n):
    answer = [[0]*n for i in range(len(num_list) // n)]

    idx = 0
    for i in range(len(num_list) // n):
        for j in range(n):
            answer[i][j] = num_list[idx]
            idx += 1
                
    return answer