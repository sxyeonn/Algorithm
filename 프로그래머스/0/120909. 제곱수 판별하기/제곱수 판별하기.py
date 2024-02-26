import math
def solution(n):
    answer = 2
    if int(math.sqrt(n)) == math.sqrt(n):
        answer = 1
    return answer