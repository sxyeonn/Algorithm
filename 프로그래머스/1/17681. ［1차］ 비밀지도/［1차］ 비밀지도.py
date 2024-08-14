def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        # 2진수 연산 진행
        num = bin(arr1[i] | arr2[i])
        # 자리수를 통일해주는 함수(zfill)
        num = num[2:].zfill(n)
        num = num.replace("1", "#")
        num = num.replace("0", " ")
        answer.append(num)
    return answer