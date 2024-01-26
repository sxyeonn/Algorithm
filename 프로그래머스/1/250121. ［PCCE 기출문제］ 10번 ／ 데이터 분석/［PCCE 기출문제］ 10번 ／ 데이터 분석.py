def solution(data, ext, val_ext, sort_by):
    answer = []
    
    for d in data:
        if ext == "code":
            if d[0] < val_ext:   # ext 값이 val_ext보다 작은 데이터
                answer.append(d)
        elif ext == "date":
            if d[1] < val_ext:   # ext 값이 val_ext보다 작은 데이터
                answer.append(d)
        elif ext == "maximum":
            if d[2] < val_ext:   # ext 값이 val_ext보다 작은 데이터
                answer.append(d)
        else:
            if d[3] < val_ext:   # ext 값이 val_ext보다 작은 데이터
                answer.append(d)
        
    
    if sort_by == "code":
        answer = sorted(answer, key=lambda x:x[0])
    elif sort_by == "date":
        answer = sorted(answer, key=lambda x:x[1])
    elif sort_by == "maximum":
        answer = sorted(answer, key=lambda x:x[2])
    else:
        answer = sorted(answer, key=lambda x:x[3])
    
    return answer