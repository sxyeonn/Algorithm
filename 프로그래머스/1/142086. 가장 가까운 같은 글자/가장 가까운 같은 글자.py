def solution(s):
    answer = []
    
    # 문자열을 순회하며 나온 문자를 하나씩 넣는 리스트
    tmp = []
    
    for i in range(len(s)):
        # 문자가 처음 나온 것이 아닐 때
        if s[i] in tmp:
            # 해당 문자가 등장한 위치를 모두 뽑아냄
            idx = [j for j, value in enumerate(tmp) if value == s[i]]
            answer.append(len(tmp) - idx[-1])
            
        # 문자가 처음 나왔을 때
        else:
            # -1로 표현
            answer.append(-1)
            
        # 등장한 문자를 tmp에 저장
        tmp.append(s[i])
    return answer