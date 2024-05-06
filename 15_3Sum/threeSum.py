def threeSum(nums):
    nums.sort()
    res = []
    sum = 0
    for i, ele in enumerate(nums):
        if(i > 0 and ele == nums[i-1]):
            continue
        l , r = i+1, len(nums) - 1
        while(l < r):  
            sum = ele + nums[l] + nums[r]
            if(sum<0):
                l+=1
            elif(sum > 0):
                r-=1
            else:
                res.append([ele, nums[l], nums[r]])
                l+=1
                while(l < r and nums[l] == nums[l-1]):
                    l+=1
               

    return res
print(threeSum([-1,0,1,2,-1,-4]))
    
    