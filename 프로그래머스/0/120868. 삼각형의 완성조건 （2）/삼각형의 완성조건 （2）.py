def solution(sides):
    answer = 0
    """
    <삼각형의 완성 조건>
    : 가장 긴 변의 길이 < 두 변의 길이의 합
    
    1. 가장 긴 변 = max(sides)
    -> max(sides) < min(sides) + a
    -> max(sides) - min(sides) < a
    
    2. 가장 긴 변 = a
    -> a < max(sides) + min(sides)
    """

    max_side = max(sides)
    min_side = min(sides)
    
    # sides에 있는 변(max_sides)이 가장 길 경우
    for new_side in range (max_side - min_side + 1, max_side + 1):
        answer += 1
        
    # 새로운 변(new_side)가 가장 길 경우
    for new_side in range (max_side + 1, max_side + min_side):
        answer += 1

    return answer