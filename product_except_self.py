def productExceptSelf(nums: list[int])-> list:
    pre, post = 1, 1
    res = [1] * len(nums)
    for i, el in enumerate(nums):
        res[i] = pre 
        pre *= el
    for i in range(len(nums) -1 , -1, -1):
        res[i] *= post
        post *= nums[i]
    return res

productExceptSelf([1,2,3,4])