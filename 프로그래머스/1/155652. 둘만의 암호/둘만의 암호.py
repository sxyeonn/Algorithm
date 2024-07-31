def solution(s, skip, index):
    answer = ''
    # 알파벳 리스트
    alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", 
                    "k", "l", "m", "n", "o", "p", "q", "r", "s", 
                    "t", "u", "v", "w", "x", "y", "z"]
    
    # skip에 있는 단어 포함 X
    for i in skip:
        alphabets.remove(i)
    
    # 문자열을 index 만큼 더해서 새로운 문자로 변경
    # z를 넘어갈 경우 a로 돌아가므로, len(alphabets) 나머지 연산 진행
    for j in s:
        tmp = alphabets[(alphabets.index(j) + index) % len(alphabets)]
        answer += tmp

    return answer