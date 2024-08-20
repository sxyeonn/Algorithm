def solution(s, n):
    answer = ''
    lower_alpha = 'abcdefghijklmnopqrstuvwxyz'
    upper_alpha = lower_alpha.upper()
    for i in s:
        # 소문자일 때
        if i in lower_alpha:
            idx = lower_alpha.index(i)
            new_idx = (idx + n) % len(lower_alpha)
            answer += lower_alpha[new_idx]
        # 대문자일 때
        elif i in upper_alpha:
            idx = upper_alpha.index(i)
            new_idx = (idx + n) % len(upper_alpha)
            answer += upper_alpha[new_idx]
        # 공백일 때
        elif i == " ":
            answer += " "
    return answer