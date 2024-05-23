# input 입력받기
N = int(input())

conf = []
for _ in range(N):
    conf.append(list(map(int, input().split())))
# print(conf) [[1, 4], [3, 5], [0, 6], [5, 7], ..]

# 끝나는 시간의 오름차순 -> 시작하는 시간의 오름차순
conf = sorted(conf, key = lambda x: (x[1], x[0]))

# print(conf) [[1, 4], [3, 5], [0, 6], ..
answer = 0
tmp = 0         # 회의가 끝나는 시간을 나타냄
for start, end in conf:
    # 회의 시작 시간이 앞선 회의가 끝나는 시간보다 크면 회의 가능
    if start >= tmp:
        answer += 1
        # 현재 회의가 끝난 시간을 tmp에 없데이트
        tmp = end
        
print(answer)
