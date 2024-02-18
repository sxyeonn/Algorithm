def solution(picture, k):
    answer = []
    
    # 각 픽셀(" ") 순회
    for p in picture:
        # 가로로 증가된 값을 mul에 저장
        mul = ''
        # " "안의 값을 순회(ex. "x.x")
        for x in range(len(p)):
            # p[0]은 x, p[1]은 ., p[2]는 x가 됨
            # p[0]을 k배 한 값을 mul에 저장
            # mul에는 "xxx...xxx"이 담김
            mul += p[x] * k
        
        # mul을 세로로 k배 확대하기 위해 k번 append 진행
        for _ in range(k):
            answer.append(mul)
        
    return answer