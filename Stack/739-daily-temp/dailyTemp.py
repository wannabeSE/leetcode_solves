def dailyTemp(temperatures: list) -> list:
    stack = [] # [temp, index]
    res = [0] * len(temperatures)
    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            stackTemp , stackIdx = stack.pop()
            res[stackIdx] = i - stackIdx
        stack.append([t, i])
    return res
print(dailyTemp([73,74,75,71,69,72,76,73]))
        # stack = [] this solution did not work
        # res = [0] * len(temperatures)
        # store = {}
        # for i, e in enumerate(temperatures):
        #     if(e not in store):
        #         store[e] = i
        # for i, t in enumerate(temperatures):
        #     while stack and t > stack[-1]:
        #         res[store[stack[-1]]] = i - store[stack[-1]]
        #         stack.pop()
        #     stack.append(t)
        # return res 
        
            
            