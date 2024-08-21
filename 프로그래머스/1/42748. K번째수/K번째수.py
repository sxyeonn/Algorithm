def solution(array, commands):
    answer = []
    for command in commands:
        # i번째부터 수부터 j번째 수까지 배열 자르기 & 정렬
        arr = sorted(array[command[0]-1:command[1]])
        # k번째 수 구하기
        answer.append(arr[command[2]-1])
    return answer