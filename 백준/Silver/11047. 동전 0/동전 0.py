# 1. 계산대 안에 있는 돈의 수와 거슬러 줄 돈을 구하기
N, K = map(int, input().split()) # N : 화폐 종류수, K : 거슬러 줄 돈

# 2. 계산대에 있는 화폐들을 리스트의 형태로 입력받기
coins = []
for _ in range(N):
    coins.append(int(input()))
coins.sort(reverse=True)

answer = 0

# 3. coin을 하나씩 순회하며 K원 만들기
for coin in coins:
    if K >= coin:   # coin은 K보다 작아야한다. 
        answer += K//coin
        K -= (coin * (K//coin))
               
print(answer)
