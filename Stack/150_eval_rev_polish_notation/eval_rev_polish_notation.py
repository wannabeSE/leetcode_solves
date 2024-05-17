def evalRPN(tokens:list) -> int:
    stack = []
    
    for i in tokens:
        if i == '+':
            stack.append(stack.pop() + stack.pop())
        elif i == '-':
            a, b = stack.pop() ,stack.pop()
            stack.append(b - a)
        elif i == '*':
            stack.append(stack.pop() * stack.pop())
        elif i == '/':
            a, b = stack.pop(), stack.pop()
            stack.append(int(b/a))
        else:
            stack.append(int(i))
    return stack[0]
print(evalRPN(["4","13","5","/","+"]))