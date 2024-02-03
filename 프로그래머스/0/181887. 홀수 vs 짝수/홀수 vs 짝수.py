def solution(num_list):
    # sum(num_list[::2]) : 홀수 원소 합
    # sum(num_list[1::2]) : 짝수 원소 합
    return sum(num_list[::2]) if sum(num_list[::2]) > sum(num_list[1::2]) else sum(num_list[1::2])