# 소수 구하는 함수
def find_num(num):
    for i in range(2, int(num**0.5)+1):
        # 소수가 아니면 break
        if num % i == 0:
            return False
    # 소수면 해당 숫자 반환
    else:
        return True     

def solution(nums):
    # 소수의 개수를 셀 count 변수
    count = 0
    
    # 3개의 수를 더함
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                number = nums[i] + nums[j] + nums[k]
                if find_num(number):
                    count += 1

    return count
