def carFleet(target: int, position: list[int], speed: list[int]) -> int:
    pair = []
    stack = []
    for i in range(len(position)):
        pair.append([position[i], speed[i]])
    for p, s in sorted(pair)[::-1]: #traversing in reverse order
        stack.append((target - p) / s)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()
    return len(stack)
print(carFleet(100, [0,2,4], [4,2,1]))