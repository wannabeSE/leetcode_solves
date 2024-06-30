def sortColors(nums: list) -> None:
    store = [0] * 3
    for c in nums:
        store[c] += 1
    r , w , b = store
    # for i in range(r):
    #     nums[i] = 0
    # for i in range(r, r+w):
    #     nums[i] = 1
    # for i in range(r+w, len(nums)):
    #     nums[i] = 2
    #? commented out lines are explicit form of below lines [used list slicing]
    nums[:r] = [0] * r
    nums[r: r+w] = [1] * w
    nums[r+w:] = [2] * b
    print(nums)
sortColors([2,0,2,1,1,0])