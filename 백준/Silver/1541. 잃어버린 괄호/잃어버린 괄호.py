# 음수 뒤에 이어지는 덧셈 연산을 괄호로 묶기
import sys
exp = sys.stdin.readline()
# 뺄셈 기호를 기준으로 연산 나누기
new_exp = exp.split('-')
sum_list = []

# 덧셈 기호가 있다면 덧셈 수행, 없으면 그 값을 sum_list에 넣음
for i in new_exp:
    if '+' in i:
        j = list(map(int, i.split('+')))
        sum_list.append(sum(j))
    else:
        sum_list.append(int(i))
        
# sum_list 안의 요소들 차례대로 뺄셈 진행
answer = sum_list[0]
for s in range(1, len(sum_list)):
    answer -= sum_list[s]
print(answer)
