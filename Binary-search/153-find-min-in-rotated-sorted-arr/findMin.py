def findMin(nums: list) -> int:
    l, r = 0, len(nums) - 1
    minimum = nums[0]
    while l <= r:
        if nums[l] < nums[r]: #if we get to a sub array that is already sorted and its left val < right val then we update the min and break the loop
            minimum = min(minimum, nums[l])  
            break
        mid = (l + r) // 2
        minimum = min(minimum,nums[mid]) 
        if nums[mid] >= nums[l]:
            l = mid + 1
        else:
            r = mid - 1
            
    return minimum

print(findMin([4,5,6,7,0,1,2]))