def largestHistogramArea(heights: list) -> int:
    stack = [] #index, height
    maxArea = 0
    for i, h in enumerate(heights):
        tracker = i
        while stack and stack[-1][1] > h:
            idx, ht = stack.pop()
            maxArea = max(maxArea, ht * (i - idx))
            tracker = idx
        stack.append([tracker, h])
    for i, h in stack:
        maxArea = max(maxArea, h * (len(heights) - i))
    return maxArea

print(largestHistogramArea([2,1,5,6,2,3]))