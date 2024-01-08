def solution(friends, gifts):
    
    # 친구들의 이름을 담은 1차원 array - friends
    # 이번 달까지 친구들이 주고받은 선물 기록을 담은 1차원 문자열 array gifts
    
    # ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]
    gift_point = {}
    
    for plus in gifts:
        names = plus.split()[0]
        if names in gift_point:
            gift_point[names] += 1
        else:
            gift_point[names] = 1    
        
    minus_point = {}
    
    for minus in gifts:
        names = minus.split()[1]
        if names in minus_point:
            minus_point[names] += 1
        else:
            minus_point[names] = 1
            
    result = {}
    
    for key in gift_point:
        if key in minus_point:
            result[key] = gift_point[key] - minus_point[key]
        else:
            result[key] = gift_point[key]
    
    answer = max(result.values())
    
    return answer

