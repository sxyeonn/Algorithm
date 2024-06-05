# 도시의 개수
N = int(input())

# 인접한 두 도시를 연결하는 도로의 길이를 왼쪽부터 제공
length = list(map(int, input().split()))

# 주요소의 리터당 가격
price = list(map(int, input().split()))

answer = 0
# 최소 금액
minPrice = price[0]

# for문을 순회하며 주유소 가격 순회
for p in range(N-1):
    # 저번 주유소보다 지금 주유소의 가격이 싸면, minPrice로 저장
    if price[p] <= minPrice:
        minPrice = price[p]
    
    # 최소 금액으로 한 도시 이동 가능 
    # 만약 해당 주유소가 저번보다 비싸다면, 그 전의 minPrice 금액으로 더 이동
    answer += (minPrice * length[p])

print(answer)