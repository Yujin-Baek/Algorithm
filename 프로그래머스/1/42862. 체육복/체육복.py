def solution(n, lost, reserve):
    
    n_lost = [l for l in lost if l not in reserve]
    n_reserve = [r for r in reserve if r not in lost]
    
    n_lost.sort()
    n_reserve.sort()
    
    answer = n - len(n_lost)
    
    for l in n_lost:
        if l-1 in n_reserve:
            answer += 1
            n_reserve.remove(l-1)
        elif l+1 in n_reserve:
            answer += 1
            n_reserve.remove(l+1)
            
    return answer