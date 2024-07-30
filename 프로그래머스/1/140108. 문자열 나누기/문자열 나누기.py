def solution(s):
    # 분해한 문자열의 개수
    answer = 0
    
    # 문자열을 분해할 수 없을 때까지 반복
    while len(s) != 0:
        yes_x, no_x = 0, 0  # x와 같은 글자 수, x와 다른 글자 수
        for i in range(len(s)):
            if s[i] == s[0]:
                yes_x += 1
            else:
                no_x += 1
            
            # 두 횟수가 같아지면 문자열 분리
            if yes_x == no_x:
                answer += 1
                s = s[i+1:]
                break
        
        else:  # for 루프가 break 없이 끝났을 때 (문자열 끝까지 갔을 때)
            answer += 1
            break
    
    return answer