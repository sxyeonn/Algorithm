def solution(n):
    answer = 0
    
    # 팩토리얼 값을 나타내는 정수 fac
    fac = 1
    # 최대값은 10! 이므로 10까지를 순회
    for i in range(1, 11):
        # 팩토리얼은 1부터 현 숫자까지의 곱을 의미
        fac *= i
        
        # 팩토리얼을 계산한 값(fac)이 n보다 작으면 그 때의 정수값(i)을 도출
        if fac <= n:
            answer = i
    return answer