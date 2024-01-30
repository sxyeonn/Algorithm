def solution(rank, attendance):
    answer = 0
    
    # rank와 출석여부로 딕셔너리 만들고 순위에 따라 정렬
    dic = dict(zip(rank, attendance))
    dic = dict(sorted(dic.items()))
    
    # 출석여부가 True인 학생의 순위 st 배열에 새롭게 저장
    st = [k for k, v in dic.items() if v is True]
    
    # 학생 순위를 통해 몇 번째 학생인지 찾아냄. 그 정보를 a, b, c에 저장
    a, b, c = rank.index(st[0]), rank.index(st[1]), rank.index(st[2])

    answer = 10000 * a + 100 * b + c
    
    return answer