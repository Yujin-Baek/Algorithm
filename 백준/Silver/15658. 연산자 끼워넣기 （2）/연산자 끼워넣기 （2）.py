N = int(input())
A = list(map(int, input().split()))
op = list(map(int, input().split()))

max_val = -float('inf')
min_val = float('inf')

stack = [(1, A[0], op[0], op[1], op[2], op[3])]

while stack:
    index, current, plus, minus, mul, div = stack.pop()

    if index == N:
        if current > max_val:
            max_val = current
        if current < min_val:
            min_val = current
        continue

    num = A[index]

    if plus:
        stack.append((index + 1, current + num, plus - 1, minus, mul, div))
    if minus:
        stack.append((index + 1, current - num, plus, minus - 1, mul, div))
    if mul:
        stack.append((index + 1, current * num, plus, minus, mul - 1, div))
    if div:
        if current < 0:
            next_val = -(-current // num)
        else:
            next_val = current // num
        stack.append((index + 1, next_val, plus, minus, mul, div - 1))

print(max_val)
print(min_val)