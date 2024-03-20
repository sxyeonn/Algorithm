def solution(score):
    answer = []
    # 학생들의 평균을 담을 배열 mean
    mean = []
    for eng, math in score:
        mean.append((eng + math) / 2)
    
    # 평균이 큰 점수가 1등이 되도록 내림차순 정렬을 한 배열 sort_mean
    sort_mean = sorted(mean, reverse=True)
    
    # mean의 각 원소가 sort_mean 배열의 몇 번째 인덱스인지 파악
    # & 그 인덱스는 순위값을 의미함
    for i in mean:
        answer.append(sort_mean.index(i) + 1)
        
    return answer