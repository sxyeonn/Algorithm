def solution(price, money, count):
    answer = 0
    use_money = 0
    for i in range(1, count+1):
        use_money += price * i
    
    if use_money - money >= 0:
        return use_money - money
    else:
        return 0

