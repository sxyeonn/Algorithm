def solution(num_str):
    # 문자열 원소 리스트로 변환하기
    num_list = list(num_str)
    
    # 리스트 원소 int형으로 변환
    num_list_int = list(map(int, num_list))
    
    # 리스트의 합 반환
    return sum(num_list_int)