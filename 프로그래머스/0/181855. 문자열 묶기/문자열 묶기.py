def solution(strArr):
    # strArr의 모든 원소 길이를 담은 배열 lenArr
    lenArr = []
    for i in strArr:
        lenArr.append(len(i))
    lenArr = sorted(lenArr)

    # lenArr의 최솟값~최댓값 순회하며, 각 값의 count 세고, max_count 찾기
    max_count = 0
    for j in range(min(lenArr), max(lenArr)+1):
        if lenArr.count(j) > max_count:
            max_count = lenArr.count(j)
    
    return max_count