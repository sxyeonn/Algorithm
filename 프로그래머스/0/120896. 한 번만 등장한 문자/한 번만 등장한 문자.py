def solution(s):
    answer = ''
    for i in s:
        # 문자열을 순회하며 각각의 count를 측정
        if s.count(i) == 1:
            answer += i
    # answer은 문자열이기 때문에 리스트화를 시켜 오름차순 정렬을 하고, join을 통해 다시 문자열로 변경
    return ''.join(sorted(list(answer)))
