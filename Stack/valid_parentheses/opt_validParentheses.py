def isValid(s: str) -> bool:
    stack = []
    closedBracketMap = {')': '(', '}': '{', ']': '['}
    for i in s:
        if i in closedBracketMap:
            if stack and stack[-1] == closedBracketMap[i]:
                stack.pop()
            else:
                return False
        else:
            stack.append(i)
    if(stack):
        return False
    else:
        return True
    #[also can be written as] return False if stack else True