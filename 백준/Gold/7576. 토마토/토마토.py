from collections import deque

def bfs():
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  
  while queue:
    y, x = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < m and 0 <= ny < n and box[ny][nx] == 0:
        box[ny][nx] = box[y][x] + 1
        queue.append([ny,nx])

m, n = map(int, input().split())

box = []

queue = deque([])

for i in range(n):
  row = list(map(int, input().split()))
  box.append(row)

for i in range(n):
  for j in range(m):
    if box[i][j] == 1:
      queue.append([i,j])

bfs()

day = -1

for row in box:
  for t in row:
    if t == 0:
      print(-1)
      exit()
    
  day = max(day, max(row))

print(day-1)