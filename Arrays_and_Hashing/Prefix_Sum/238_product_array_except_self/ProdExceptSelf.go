package main

import (
	"fmt"
	"slices"
)

func productExceptSelf(nums []int) []int {
	prefix := make([]int, len(nums))
	postfix := make([]int, len(nums))
	prefix[0] = nums[0]
	postfix[len(nums)-1] = nums[len(nums)-1]
	for i := 1; i < len(nums); i++ {
		prefix[i] = prefix[i-1] * nums[i]
	}
	for i := len(nums) - 2; i >= 0; i-- {
		postfix[i] = postfix[i+1] * nums[i]
	}
	nums[0] = postfix[0] //[1 2 6 24]
	nums[len(nums)-1] = prefix[len(nums)-2] //[24 24 12 4]
	for i := 1; i < len(nums)-1; i++ {
		nums[i] = prefix[i-1] * postfix[i+1]
	}
	return nums
}
//no need to write it unless you're being extra
func productExceptSelfOpt(nums []int) []int {
	pre, post := 1, 1
	res := make([]int, len(nums))
	for i := range res {
		res[i] = 1
	}
	for i, v := range nums {
		res[i] = pre
		pre *= v
	}
	for i, v := range slices.Backward(nums) {
		res[i] *= post
		post *= v
	}
	return res
}
func main() {
	fmt.Println("!Opt", productExceptSelf([]int{1, 2, 3, 4}))
	fmt.Println(productExceptSelfOpt([]int{1, 2, 3, 4}))
}
