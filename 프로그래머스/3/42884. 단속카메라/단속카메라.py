def solution(routes):
    routes.sort(key=lambda x: x[1])
    
    camera = float("-inf")
    count = 0

    for route in routes:
        if camera < route[0]:
            camera = route[1]
            count += 1

    return count
