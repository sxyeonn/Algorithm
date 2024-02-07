def solution(myStr):
    answer = []
    myStr = myStr.replace("b", "a")
    myStr = myStr.replace("c", "a")
    myStr = myStr.split("a")
    for x in myStr:
        if x:
            answer.append(x) 
    if answer == []:
        answer.append("EMPTY")
    return answer