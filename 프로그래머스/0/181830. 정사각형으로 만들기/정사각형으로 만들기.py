def solution(arr):
    
    # 행의 수
    row = len(arr)
    # 열의 수
    col = len(arr[0])
    # 행과 열 중 큰 수를 num에 저장 
    num = row if row > col else col
    
    # num이 행보다 크면.. 열의 수가 더 많으므로, 행을 추가함
    if num > row:
        for i in range(num-row):
            arr.append([0] * col)
    
    # num이 열보다 크면.. 행의 수가 더 많으므로, 열을 추가함
    if num > col:
        for j in range(num):
            # num-col만큼 각 열에 0을 추가 
            for a in range(num-col):
                arr[j].append(0)

    return arr