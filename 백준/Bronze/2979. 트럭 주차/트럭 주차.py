# 주차요금 A, B, C
price = list(map(int, input().split()))

times = []
# 트럭이 주차장에 도착한 시간과 떠난 시간
for _ in range(len(price)):
    times.append(list(map(int, input().split())))
    
res = [0] * 100
for i, j in times:
    for r in range(i, j):
        res[r] += 1      

answer = 0
for p in range(len(price)):
    answer += (res.count(p+1) * price[p] * (p+1))
    
print(answer)