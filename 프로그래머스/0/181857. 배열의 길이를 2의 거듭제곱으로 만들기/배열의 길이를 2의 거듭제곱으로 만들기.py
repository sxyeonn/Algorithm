def solution(arr):
    app = 0
    
    #if len(arr) >= 1000:
    #    return arr
    
    if len(arr) > 512:
            app = 1024-len(arr)
            
    else:
        for i in range(10):
            if 2**i == len(arr):
                return arr
            elif 2**i > len(arr):
                app = 2**i - len(arr)
                break
        
    
    for j in range(app):
        arr.append(0)
        
    return arr