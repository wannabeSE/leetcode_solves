
def two_sum(nums, target):
    store={}
    for i, n in enumerate(nums):
        diff = target-n
        if diff in store:
            return [store[diff], i]
        store[n] =i
        
print('sol->',two_sum([3,3],6))