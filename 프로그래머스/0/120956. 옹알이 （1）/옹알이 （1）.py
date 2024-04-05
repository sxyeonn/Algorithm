
def solution(babbling):
    words = ["aya", "ye", "woo", "ma"]
    for b in range(len(babbling)):
        for w in words:
            
            # 순회를 하며, ex. wyeoo -> ye를 ' '으로 변경 -> w oo로 변경 (ye를 빈칸으로만 변경하면 woo가 되어 woo가 또 없어짐! )
            babbling[b] = babbling[b].replace(w, ' ')
        
        babbling[b] = babbling[b].replace(' ', '')
    
    return babbling.count('')