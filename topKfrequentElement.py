def topKFrequents(nums: list[int], k: int):
    frequency = {} 
    store = []
    for i in range(len(nums)+1):
        store.append([])
    for i in nums:
        frequency[i] = 1 + frequency.get(i, 0)
    for number,count in frequency.items():
        store[count].append(number)

    result = []
    print(store)
    for i in range(len(store)-1, 0, -1): #traversing in reverse order cause in this way we will get the max occurrence faster 
        for j in store[i]: #O(k*log(n))
            result.append(j)
            if len(result) == k:
                return result


print(topKFrequents([1],1))