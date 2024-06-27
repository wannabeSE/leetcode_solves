class Solution:
    def reverser(self, p1, p2, nums, startPoint, endPoint):
        for i in range(startPoint, endPoint):
            if(p1 != p2 and p1 < p2):
                temp = nums[p1]
                nums[p1] = nums[p2]
                nums[p2] = temp
            p1+=1
            p2-=1
        return nums
    def rotate(self, nums: list[int], k: int):
        if(k > len(nums)):
            k = k%len(nums)
        self.reverser(0, len(nums) - 1 - k, nums, 0, len(nums) - k - 1)
        self.reverser(p1=len(nums) - k, p2=len(nums) - 1, nums=nums, startPoint=len(nums) - k, endPoint=len(nums))
        self.reverser(0, len(nums)-1, nums, 0, len(nums))
        print(nums)
t = Solution()
t.rotate([1,2,3,4,5,6], 11)
