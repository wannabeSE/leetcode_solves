def findMedianSortedArrays(nums1: list, nums2: list) -> float:
    size1, size2 = len(nums1) , len(nums2)
    totalSize = size1 + size2
    onLeft = (size1 + size2 + 1) // 2
    if size1 > size2:
        return findMedianSortedArrays(nums2, nums1) #!swapping the arrays is a must do
    low, high = 0, size1
    while low <= high:
        mid1 = (low + high) // 2
        mid2 = onLeft - mid1
        r1 = nums1[mid1]  if mid1 < size1 else float('inf')
        r2 =  nums2[mid2] if mid2 < size2 else float('inf')
        l1 = nums1[mid1 - 1] if mid1 - 1 >= 0 else float('-inf')
        l2 =  nums2[mid2 - 1] if mid2 - 1 >= 0 else float('-inf')
        if l1 <= r2 and l2 <= r1:
            if totalSize % 2 == 0:
                return (max(l1, l2) + min(r1, r2)) / 2 
            return max(l1, l2)
        elif l1 > r2:
            high = mid1 - 1
        else:
            low = mid1 + 1
print(findMedianSortedArrays([1,2], [3,4]))