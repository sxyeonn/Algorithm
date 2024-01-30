def solution(arr, query):
    for i in range(len(query)):
        if i%2==0:  # 짝수 인덱스
            # arr에서 query[i]번 인덱스를 제외하고 배열의 query[i]번 인덱스 뒷부분을 버림
            #print(arr[query[i]]) # -> 4번 인덱스를 제외하고 뒤를 버림 => 4 이후로 버림
            arr = arr[:query[i]+1]
            
        else:       # 홀수 인덱스
            # arr에서 query[i]번 인덱스를 제외하고 배열의 query[i]번 인덱스 앞부분을 버림
            # 1번 인덱스를 제외하고 앞을 버림 -> 1번 인덱스 값 = 1
            # ==> 1의 앞부분인 0을 버림
            arr = arr[query[i]:]
        
    return arr