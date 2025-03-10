from itertools import permutations

n, m = map(int, input().split())
arr = [i for i in range(1, n + 1)]

result = []

for p in permutations(arr, m):
    if list(p) == sorted(p):
        result.append(p)

for seq in result:
    print(' '.join(map(str, seq)))
