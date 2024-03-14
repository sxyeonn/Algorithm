def solution(polynomial):
    x_num, num = 0, 0

    for i in polynomial.split(' '):
        if 'x' in i:
            if i[:-1] != "":
                x_num += int(i[:-1])
            else:
                x_num += 1
        elif i != "+":
            num += int(i) 
    
    if x_num == 1:
        x_num = "x"
    elif x_num > 1:
        x_num = str(x_num) + "x"
    else:
        x_num = ""
        
    if num == 0:
        num = ""
    elif x_num == "":
        num = str(num)
    else:
        num = " + " + str(num)

    return x_num+num