def solution(array):
    answer = 0
    
    # 중복을 없앤 리스트 set_list
    set_list = list(set(array))
    
    # 원소 count 개수를 담을 num_count
    num_count = [0] * len(set_list)
    
    # 중복이 없는 리스트 set_list를 순회하며..
    # set_list의 원소 각각이 본래 list인 array에 몇 번있는지 확인
    # -> 이 값을 num_count 배열에 차례대로 저장
    for i in range(len(set_list)):
        num_count[i] = array.count(set_list[i])
    
    # set_list:  [1, 3, 5, 7]
    # num_count:  [2, 2, 3, 2]
    # num_count 배열에서 최빈값을 가진 값의 인덱스 
    # (위의 예시일 때 값은 2(최빈값이 3이므로, 숫자 3의 인덱스는 2임))
    mode_idx = num_count.index(max(num_count))
    
    # 횟수를 담은 배열에서 최빈값이 1개가 아니면 answer = -1
    if num_count.count(max(num_count)) != 1:
        answer = -1
    
    # 최빈값이 아니면, set_list에서 최빈값 인덱스에 해당하는 값을 뽑아옴
    else:
        answer = set_list[mode_idx]
    
    return answer