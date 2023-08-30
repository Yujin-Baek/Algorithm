def dfs(depth, idx):
    if depth == 6:
        print(*result)
        return
    for i in range(idx, k):
        result.append(S[i])
        dfs(depth+1, i+1)
        result.pop()
    
while True:
    input_data = list(map(int, input().split()))
    k = input_data[0]
    if k == 0:
        break
    S = input_data[1:]
    result = []
    dfs(0, 0)
    print()