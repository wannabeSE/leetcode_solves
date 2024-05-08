def maxArea(height: list) -> int:
    l, r = 0, len(height) - 1
    maxArea = 0
    while(l < r):
        currMin = min(height[l], height[r])
        if(currMin == height[l]):
            area = currMin * (r - l)
            l+=1
        elif(currMin == height[r]):
            area = currMin * (r - l)
            r-=1
        maxArea = max(area, maxArea)
    return maxArea 
        
print(maxArea([0,1,0,2,1,0,1,3,2,1,2,1]))