def solution(arr)
    
    # 행의 수
    col = len(arr)
    
    # 열의 수
    row = len(arr[0])
    
    # 행과 열 중 큰 수를 num에 저장 
    num = col if col  row else row
    
    # num이 열의 수보다 크면.. 행의 수가 더 많으므로, 모자란 열을 원소 0으로 추가함
    if num  row
        for j in range(num)
        
        	# 추가해야하는 열의 개수는 num-row개
            for _ in range(num-row)
                arr[j].append(0)
                
    # num이 행의 수보다 크면.. 열의 수가 더 많으므로, 모자란 행(큰 수 - 행 수)을 추가함. 이 때, 추가하는 행의 원소 개수는 큰 수(열의 개수) 만큼임
    if num  col
        for i in range(num-col)
            arr.append([0]  row)
    
    
    
    return arr