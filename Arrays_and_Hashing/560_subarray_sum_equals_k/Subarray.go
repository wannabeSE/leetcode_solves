package main

import "fmt"

func subArraySum(nums []int, k int) int {
	var (
		count, preSum = 0, 0
		prefixSumFreq = make(map[int]int, len(nums))
	)
	prefixSumFreq = map[int]int{
		0: 1,
	}
	if len(nums) == 1 && nums[0] == k {
		return 1
	}
	for _, v := range nums {
		preSum += v //prefix summation
		exclude := preSum - k
		count += prefixSumFreq[exclude]
		prefixSumFreq[preSum]++
	}
	return count
}

func main() {
	fmt.Println(subArraySum([]int{-1, -1, 1}, 0))
}
