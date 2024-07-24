import sys
N = int(sys.stdin.readline())
S = set()

for _ in range(N):
    temp = sys.stdin.readline().strip().split()
    
    # 연산이 add, empty면 연산만 주어진다. 
    if len(temp) == 1:
        if temp[0] == 'all':
            S = set([i for i in range(1, 21)])
        elif temp[0] == 'empty':
            S = set()
    
    # 연산명에 따라 연산 수행
    else:
        func = temp[0]
        x = int(temp[1])

        if func == 'add':
            S.add(x)
        elif func == 'remove':
            S.discard(x)
        elif func == 'check':
            print(1 if x in S else 0)
        elif func == 'toggle':
            if x in S:
                S.discard(x)
            else:
                S.add(x)