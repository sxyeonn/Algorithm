def solution(num, total):
    answer = []
    
    # x + x+1 + x+2 + ..
    # => nx + (1+2+..+n) = total
    # nx = total-tmp
    # x = (total-tmp)//n
    tmp = 0
    for i in range(num):
        tmp += i
    print(tmp, total-tmp, (total-tmp)//num)
    start_num = (total-tmp)//num
    answer = [_ for _ in range(start_num, start_num+num)]
    return answer