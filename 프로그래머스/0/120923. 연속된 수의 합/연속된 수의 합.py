def solution(num, total):
    answer = []
    tmp = 0
   	# x + (x+1) + (x+2) + (x+3) ... = total
    # nx + (1+2+..+n) = total
    
    # (1+2+..+n) = tmp
    for i in range(num):
        tmp += i
    
    # 연속된 수 중 처음 수 start_num
    start_num = (total-tmp)//num
    
    # start_num부터 1씩 더해 num개의 연속된 수 구하기
    answer = [_ for _ in range(start_num, start_num+num)]
    return answer