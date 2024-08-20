def solution(s, n):
    answer = ''
    lower_alpha = 'abcdefghijklmnopqrstuvwxyz'
    
    for i in s:
        # 공백일 때
        if i == " ":
            answer += " "
        
        # 문자일 때(소문자, 대문자 모두)
        else:
            # 현재 문자를 소문자로 바꿔 위치를 찾음
            idx = lower_alpha.index(i.lower())
            # 새로운 위치 찾기
            new_idx = (idx + n) % len(lower_alpha)
            # 새로운 문자 찾기
            tmp = lower_alpha[new_idx]
            # 소문자일 때
            if i in lower_alpha:
                answer += tmp
            # 대문자일 때
            else:
                answer += tmp.upper()
        
    return answer