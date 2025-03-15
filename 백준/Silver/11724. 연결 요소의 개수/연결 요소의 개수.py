import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(start):
  visited[start] = True
  for next in graph[start]:
    if not visited[next]:
      dfs(next)

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

visited = [False] * (n+1)

for i in range(m):
  u,v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

count = 0

for i in range(1, n+1):
  if not visited[i]:
    dfs(i)
    count += 1

print(count)