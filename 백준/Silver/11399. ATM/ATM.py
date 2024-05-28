import sys

# 문제 입력받기
N = int(input())
lines = list(map(int, sys.stdin.readline().split()))
lines.sort()

sum_list = [0]
# 누적합 구하기
for line in lines:
    tmp = line + sum_list[-1]
    sum_list.append(tmp)
    
print(sum(sum_list))