def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    
    for i in range(len(numbers)):
        # 현재 스택의 가장 위에 있는 숫자가 현재 num보다 크지 않으면 스택에 push
        # 현재 스택의 가장 위에 있는 숫자가 현재 num보다 크다면 answer의 해당 숫자 위치를 num으로 변경하고 스택에서 pop
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack[-1]] = numbers[i]
            stack.pop()
        stack.append(i)
        
    return answer