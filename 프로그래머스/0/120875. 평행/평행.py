def solution(dots):

    # 기울기가 같으면 평행(기울기 = y좌표차이/x좌표차이)
    # 3개의 조건: 12/34    13/24    14/23

    g1 = (dots[1][1]-dots[0][1]) / (dots[1][0]-dots[0][0])
    g2 = (dots[3][1]-dots[2][1]) / (dots[3][0]-dots[2][0])
    
    g3 = (dots[2][1]-dots[0][1]) / (dots[2][0]-dots[0][0])
    g4 = (dots[3][1]-dots[1][1]) / (dots[3][0]-dots[1][0])
    
    g5 = (dots[3][1]-dots[0][1]) / (dots[3][0]-dots[0][0])
    g6 = (dots[2][1]-dots[1][1]) / (dots[2][0]-dots[1][0])
    
    if g1==g2 or g3==g4 or g5==g6:
        return 1
    else:
        return 0