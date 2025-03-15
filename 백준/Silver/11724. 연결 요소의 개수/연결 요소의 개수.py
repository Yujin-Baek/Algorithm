import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(start):
  visited[start] = True
  for i in range(1, n+1):
    if graph[start][i] == 1 and not visited[i]:
      dfs(i)

n, m = map(int, input().split())

graph = [[0 for _ in range(n+1)] for _ in range(n+1)]

visited = [False] * (n+1)

for i in range(m):
  u,v = map(int, input().split())
  graph[u][v] = 1
  graph[v][u] = 1

count = 0

for i in range(1, n+1):
  if not visited[i]:
    dfs(i)
    count += 1

print(count)