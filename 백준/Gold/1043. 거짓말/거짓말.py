import sys
input = sys.stdin.readline

def find(parent, x):
    if x != parent[x]:
        parent[x] = find(parent, parent[x])

    return parent[x]

def union(parent, a, b, truth):
    rootA = find(parent, a)
    rootB = find(parent, b)

    if rootA in truth and rootB in truth:
        return

    if rootA in truth:
        parent[rootB] = rootA
    
    elif rootB in truth:
        parent[rootA] = rootB
    
    else:
        if rootA < rootB:
            parent[rootB] = rootA
        
        else:
            parent[rootA] = rootB


n, m = map(int, input().split())
truth = list(map(int, input().split()))[1:]

parties = []
parent = list(range(n+1))

for _ in range(m):
    party_info = list(map(int, input().split()))
    party_len = party_info[0]
    party = party_info[1:]
    
    for i in range(party_len - 1):
        union(parent, party[i], party[i+1], truth)
    
    parties.append(party)
    
ans = 0
for party in parties:
    for i in range(len(party)):
        if find(parent, party[i]) in truth:
            break
    else:
      ans += 1

print(ans)