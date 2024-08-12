def solution(park, routes):
    answer = []
    # 동, 서, 남, 북 방향을 표시함
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    types = ["E", "W", "S", "N"]
    
    # 공원의 길이
    h = len(park)
    w = len(park[0])
    
    # 시작 지점은 S
    for i in range(h):
        if "S" in park[i]:
            x = i
            y = park[i].index("S")
            break
    
    for r in routes:
        r = r.split(' ')
        op = r[0]
        n = int(r[1])
        
        print("어디로 이동?: ", op, n)
        
        nx, ny = x, y
        for _ in range(n):
            nx += dx[types.index(op)]
            ny += dy[types.index(op)]

            
            # 공간을 벗어나는 경우 무시
            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                break
                
            # 장애물을 만난 경우 무시
            if park[nx][ny] == "X":
                break
                
        
        else:
            # 명령 수행
            x, y = nx, ny
                
        print(nx, ny)
        print("---------")
    
    answer.append(x)
    answer.append(y)

    return answer