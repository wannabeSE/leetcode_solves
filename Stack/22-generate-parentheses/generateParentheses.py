def generateParentheses(n: int) -> list[str]:
    stack = []
    res = []
    def backtrack(openP, closeP):
        if openP == closeP == n:
            res.append(''.join(stack))
            return
        if openP < n:
            stack.append('(')
            backtrack(openP + 1, closeP)
            print(stack)
            stack.pop()
            print('after pop',stack)
        if openP > closeP:
            stack.append(')')
            backtrack(openP , closeP + 1)
            print(stack)
            stack.pop()
            print('after pop',stack)
    backtrack(0, 0)
    return res
        
print(generateParentheses(3))