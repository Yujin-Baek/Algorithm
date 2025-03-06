def solution(dirs):
    udrl = {'U': (1, 0), 'D': (-1, 0), 'R': (0, 1), 'L': (0, -1)}
    
    x, y = 0, 0
    
    history = set()
    
    for dir in dirs:
        ny = y + udrl[dir][0]
        nx = x + udrl[dir][1]
        
        if -5 <= ny <= 5 and -5 <= nx <= 5:
            history.add(((y, x), (ny, nx)))
            history.add(((ny, nx), (y, x)))
            y = ny
            x = nx
    return len(history)//2