def solution(keyinput, board):
    # 첫 시작은 0, 0
    answer = [0, 0]
    lim_x, lim_y = board[0]//2, board[1]//2
    direction = {'up' : [0, 1], 'down' : [0, -1], 'left' : [-1, 0], 'right' : [1, 0]}
    for i in keyinput:
        dx, dy = direction[i]
        # 만약 이동 후의 x좌표 값이 맵 가로 길이의 반보다 크거나, 
        # 이동 후의 y좌표 값이 맵 세로 길이의 반보다 크면 수행하지 않고 넘어감
        # -> 키 입력을 받아도 좌표가 이동되지 않음
        if abs(answer[0] + dx) > lim_x or abs(answer[1]+dy) > lim_y:
            continue
        else:
            answer[0] += dx
            answer[1] += dy
            
    return answer