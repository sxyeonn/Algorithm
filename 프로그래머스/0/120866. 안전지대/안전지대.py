def solution(board):
    answer = 0
    # 지뢰의 인덱스를 담은 배열 land_arr
    land_arr = []
    
    # 지뢰의 인덱스를 찾아서 land_arr 배열에 담음
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                land_arr.append([i,j])
                
    # 위, 우측 위 대각선, 오른쪽, 오른쪽 아래 대각선, 아래, 좌측 아래 대각선, 왼쪽, 좌측 위 대각선
    direction = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
    
    # 지뢰의 인덱스에서 각 방향 값을 더해, 그 값을 1로 채움 -> 위험지역이 1로 변경됨
    for l in land_arr:
        for x, y in direction:
            if 0 <= (l[0] + x) < len(board) and 0 <= (l[1] + y) < len(board):
                board[l[0] + x][l[1] + y] = 1
    
    # 위험지역을 제외한 지역(원소가 0)을 찾아 개수를 센다. 
    for b in board:
        answer += b.count(0)   
    
    return answer