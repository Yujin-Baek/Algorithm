from collections import deque

dx = [0, 0, -1, 1, 0, 0]
dy = [-1, 1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs():
    while queue:
        z, y, x = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0<=nx<m and 0<=ny<n and 0<=nz<h and tomato[nz][ny][nx] == 0:
                tomato[nz][ny][nx] = tomato[z][y][x] + 1
                queue.append((nz, ny, nx))

m, n, h = map(int, input().split())
tomato = [[list(map(int, input().split())) for i in range(n)] for j in range(h)]

queue = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 1:
                queue.append((i, j, k))

bfs()

all_tomato = True

days = -1

for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 0:
                all_tomato = False
                break
            days = max(days, tomato[i][j][k])

if all_tomato:
    print(days - 1)
else:
    print(-1)


