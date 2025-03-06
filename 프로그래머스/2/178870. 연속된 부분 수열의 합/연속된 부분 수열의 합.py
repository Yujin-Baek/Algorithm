def solution(sequence, k):
    answer = []
    
    min = float("inf")
    
    start = 0
    end = 0
    cum_sum = sequence[start]
    
    while end < len(sequence):
        if cum_sum == k:
            if end - start < min:
                min = end - start
                answer = [start, end]
            cum_sum -= sequence[start]
            start += 1
        elif cum_sum < k:
            end += 1
            if end < len(sequence):
                cum_sum += sequence[end]
        else:
            cum_sum -= sequence[start]
            start += 1
        
    return answer