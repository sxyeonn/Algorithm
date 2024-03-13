def solution(numbers):
    # 제공된 배열을 정렬한다. 
    numbers.sort()
    # 가장 작은 수 2개를 곱한 값과 가장 큰 수를 곱한 값 중 더 큰 값을 return 한다. 
    return max(numbers[0]*numbers[1], numbers[-1]*numbers[-2])