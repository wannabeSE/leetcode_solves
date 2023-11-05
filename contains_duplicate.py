def contains_duplicate(nums):

    duplicate = set()
    for i in range(len(nums)):
        if nums[i] not in duplicate:
            duplicate.add(nums[i])
        else:
            return True
        
    return False
def dupZ(arr)-> bool:
    #flag: bool = False
    arr.sort()
    for i in range(len(arr)-1):
        if(arr[i] == arr[i+1]):
            return True
    return False
print(contains_duplicate([1,2,3,4]))

print(dupZ([1,2,3,4]))