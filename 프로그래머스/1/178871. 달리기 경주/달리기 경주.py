def solution(players, callings):
    
    dic = {player: i for i, player in enumerate(players)} # 선수: 등수
    for call in callings:   # 불리는 선수들 순회
        idx = dic[call]     # idx는 현재 불린 선수 인덱스
        players[idx], players[idx-1] = players[idx-1], players[idx] # 순서 변경
        
        dic[call] -= 1      # 불린 선수 인덱스 변경(순위 앞으로)
        dic[players[idx]] += 1     # 앞 선수가 뒤로 추월(순위 뒤로)
        # idx로 해야함!
        
        # players[idx], players[idx-1] = players[idx-1], players[idx] 
    return players