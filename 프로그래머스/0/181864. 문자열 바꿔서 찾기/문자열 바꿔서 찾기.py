def solution(myString, pat):
    s = ""
    for i in myString:
        if i == "A":
            s += "B"
        else:
            s += "A"
    if pat in s:
        return 1
    return 0