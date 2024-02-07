def solution(myString, pat):
    answer = 0
    for i in range(len(myString)-len(pat)+1):
        # myString을 순회하며, pat의 길이만큼 자른다. 
        # 그것이 pat과 같으면 값을 하나 올린다. 
        if pat in myString[i:i+len(pat)]:
            answer += 1        
    return answer