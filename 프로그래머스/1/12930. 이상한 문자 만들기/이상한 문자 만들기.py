def solution(s):
    answer = ''
    # 공백을 기준으로 문자를 나눠 리스트에 저장
    words = s.split(' ')
    for word in words:
        for w in range(len(word)):
            # 홀수번째 알파벳은 소문자로 변경
            if w % 2 != 0:
                answer += word[w].lower()
            
            # 짝수번째 알파벳은 대문자로 변경
            else:
                answer += word[w].upper()
        
        # 공백 추가
        answer += ' '
    # 마지막 단어에도 공백이 추가되므로, 마지막 공백 제거하고 반환
    return answer[:-1]