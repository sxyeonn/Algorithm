def solution(x):

    tmp = 0
    for i in str(x):
        tmp += int(i)
    if (x / tmp) == round((x / tmp)):
        return True
    else:
        return False
