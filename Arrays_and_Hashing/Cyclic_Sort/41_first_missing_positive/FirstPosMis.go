package main

import (
	"fmt"
)

func firstMissingPositive(nums []int) int {
	for i := range len(nums) {
		// swapping should be performed
		// if the element is a positive number and
		// greater than 0 (we're only interested in positive missing numbers and
		// we do not want the index to go out of bound for rest of the conditions in the loop)
		// if the element is not in it's home index (element == index + 1)
		// swapping should not be performed
		// if the element is greater than the length of the array
		// because there is no home index for that element
		for nums[i] >= 1 && nums[i] <= len(nums) && nums[i] != nums[nums[i]-1] {
			nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
		}
	}
	//unmatched element is the missing number
	for i, v := range nums {
		if v != i+1 {
			return i + 1
		}
	}
	return len(nums) + 1
}
func main() {
	cases := [][]int{{1, 1}, {2, 2}, {1, 2, 2, 1, 3, 1, 0, 4, 0}, {7, 8, 9, 11, 12}, {3, 4, -1, 1}}
	for _, v := range cases {
		fmt.Println(firstMissingPositive(v))
	}

}
