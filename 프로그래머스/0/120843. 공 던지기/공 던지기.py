def solution(numbers, k):

    new_numbers = numbers * (k-1)
    answer = new_numbers[2*(k-1)]
    
    return answer