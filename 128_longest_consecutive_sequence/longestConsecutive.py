def longestConsecutive(nums: list) -> int:
    numSet = set(nums) 
    longest = 0
    for num in numSet:
        if (num-1) not in numSet: #look up in set takes O(1)
            length = 0
            while(num + length) in numSet:
                length+=1
            longest = max(longest, length)
    return longest
print(longestConsecutive([100,4,200,1,3,2,2]))