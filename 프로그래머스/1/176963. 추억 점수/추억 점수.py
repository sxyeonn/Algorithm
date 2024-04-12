def solution(name, yearning, photo):
    # photo의 길이만큼 기본 answer 배열 생성
    answer = [0] * len(photo)
    
    # 인물과 추억 점수로 딕셔너리 생성
    score_dic = dict(zip(name, yearning))
    
    for p in range(len(photo)):
        # 각 사진 중 정보가 있는 인물에 대해 추억점수를 더함
        for i in photo[p]:
            if i in name:
                answer[p] += score_dic[i]
    return answer