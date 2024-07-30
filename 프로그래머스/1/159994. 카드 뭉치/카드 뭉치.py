def solution(cards1, cards2, goal):

    c1, c2 = 0, 0
    for i in goal:
        if i in cards1:
            if c1 != cards1.index(i):
                return "No"
            c1 += 1
        else:
            if c2 != cards2.index(i):
                return "No"
            c2 += 1
        
    return "Yes"