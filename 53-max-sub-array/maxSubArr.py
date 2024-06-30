def maxSubArr(nums: list) -> int:
    res = nums[0]
    currSum = 0
    for n in nums:
        currSum = max(currSum, 0) #? if currSum is less than 0 we reset it to 0
        currSum += n
        res = max(currSum, res) #? checking the which one is the max, res or the currSum
    return res
print(maxSubArr([-2,1,-3,4,-1,2,1,-5,4]))