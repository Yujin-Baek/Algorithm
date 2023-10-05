from collections import defaultdict

def bfs():
    visited = []
    
    queue = [v]
    visited.append(v)
    
    while queue:
        now = queue.pop(0)
        print(now, end=' ')
        for i in graph[now]:
            if i not in visited:
                visited.append(i)
                queue.append(i)

def dfs(node, visited = []):
  visited.append(node)
  print(node, end=' ')

  for i in graph[node]:
    if i not in visited:
      dfs(i, visited)

n, m, v = map(int, input().split())

graph = defaultdict(list)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

dfs(v)
print()
bfs()