def solution(a, b, n):
    answer = 0
    while n >= a:
        # 마트에 가져가고 남은 빈 병
        remain = n % a
        # 빈 병을 내서 새로 받은 콜라 개수
        new = (n // a) * b
        answer += new
        # 현재 병 개수는 남은 빈 병 + 새로 받은 콜라
        n = new + remain
    return answer