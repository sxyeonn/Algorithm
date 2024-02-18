def solution(n):
    dy = [0,1,0,-1] # 오른,아래,왼,위
    dx = [1,0,-1,0]

    arr = [ [0 for x in range(n)] for _ in range(n)]

    x=0
    y=0
    arr[y][x] = 1
    cnt = 2

    k=0

    while cnt<=n*n:
        while 1:
            ny = y + dy[k] 
            nx = x + dx[k]

            if ny<0 or ny >=n or nx<0 or nx >=n or arr[ny][nx]!=0:
                break

            y = ny
            x = nx

            arr[y][x]= cnt
            cnt+=1

        k = (k+1) % 4

    return arr