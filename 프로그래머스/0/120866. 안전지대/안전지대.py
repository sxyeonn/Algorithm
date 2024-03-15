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
    
    for l in land_arr:
        # 지뢰 인덱스로 board 배열 접근
        #print(board[l[0]][l[1]])
        for x, y in direction:
            #print(l[0] + x, l[1] + y, len(board))
            if 0 <= (l[0] + x) < len(board) and 0 <= (l[1] + y) < len(board):
                #print(l[0] + x, l[1] + y)
                board[l[0] + x][l[1] + y] = 1
    # 지뢰 인덱스로 board 배열 접근
    #print(board[land_arr[0][0]][land_arr[0][1]])
    
    
    for b in board:
        answer += b.count(0)   
    
    return answer