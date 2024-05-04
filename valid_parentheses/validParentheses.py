def isValid(s: str) -> bool:
    stack = []
    flag = False
    if(len(s)%2 != 0):
        return flag
    for ele in s:
        if(ele == '(' or ele == '{' or ele == '['):
            stack.append(ele)
        elif((ele == ')' or ele == '}' or ele == ']') and len(stack) != 0):
            prev = stack.pop()
            if(ele == ')' and prev == '('):
                flag = True
            elif(ele == '}' and prev == '{'):
                flag = True
            elif(ele == ']' and prev == '['):
                flag = True
            else:
                return False
        else:
            return False

    if(len(stack) != 0):
        return False
    else: 
        return flag
            
print(isValid('()'))