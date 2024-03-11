def solution(dots):
    answer = 0
    # dots 배열의 가장 마지막 원소를 기준점으로 잡음
    standard = dots.pop()
    # 가장 마지막 원소가 빠진 dots 배열을 순회하며..
    for x, y in dots:
        # 기준점과 x좌표가 같은 좌표는 세로의 길이(y좌표의 차이)를 구함
        if x == standard[0]:
            length = abs(y-standard[1])
        # 기준점과 y좌표가 같은 좌표는 가로의 길이(x좌표의 차이)를 구함
        if y == standard[1]:
            width = abs(x-standard[0])
    return length * width