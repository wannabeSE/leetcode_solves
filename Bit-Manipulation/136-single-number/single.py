def singleNumber(nums: list) -> int:
    res = 0
    for n in nums:
        res = res ^ n
    return res
print(singleNumber([2,2,1]))