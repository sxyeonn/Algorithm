def solution(nums):

    # 이론적으로 가질 수 있는 폰켓몬 수(N/2)
    num = len(nums) // 2
    
    if num < len(set(nums)):
        return num
    else:
        return len(set(nums))
