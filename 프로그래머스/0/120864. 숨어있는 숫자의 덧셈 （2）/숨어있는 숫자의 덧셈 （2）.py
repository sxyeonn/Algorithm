import re
def solution(my_string):
    answer = 0
    # 정규표현식 사용
    m = re.compile('[0-9]+')
    
    # 자연수만 담은 리스트 num_list
    num_list = m.findall(my_string)
    
    # num_list의 모든 원소의 합 계산
    for i in num_list:
        answer += int(i)
    # sum(int(i) for i in num_list)
    return answer