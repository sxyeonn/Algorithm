def solution(s):
    answer = 0
    
    # 공백에 따라 원소를 구분한 새로운 리스트 new_s
    new_s = s.split(" ")
    for i in range(len(new_s)):     
        if new_s[i] == "Z":
            # 원소가 Z이면 그 전 값을 뺌
            answer -= int(new_s[i-1])
        else:
            # 원소가 Z가 아니면 값을 더함
            answer += int(new_s[i])
        
    return answer