package main

import "fmt"

// Better but still uses extra space
func majorityElement(nums []int) int {
	freq := make(map[int]int)
	mEle := 0
	for _, ele := range nums {
		//incrementing the frequency of the current element
		freq[ele]++
		// we should check if the current element's frequency is
		// higher than the n/2
		// if yes then we store the element as major element
		if freq[ele] > len(nums)/2 {
			mEle = ele
		}
	}
	return mEle
}

// Optimal and does not use any extra space
// the idea is to start increasing the count for the first element
// we encounter and store it in variable
// then decrease the count if
// we encounter a different element other than the previous element
// when the count becomes 0 we should reassign it to the variable (ele)
func majorityElementMoore(nums []int) int {
	count, ele := 0, nums[0]
	for i := 1; i < len(nums); i++ {
		if ele == nums[i] {
			count++
		} else if count == 0 {
			ele = nums[i]
		} else {
			count--
		}
	}
	count = 0
	for _, v := range nums {
		if ele == v {
			count++
		}
	}
	if count > len(nums)/2 {
		return ele
	}
	return 0
}
func main() {
	cases := [][]int{{2, 2, 1, 1, 1, 2, 2}, {3, 2, 3}, {3, 3, 4}, {6, 5, 5}}
	for _, c := range cases {
		fmt.Println(majorityElementMoore(c))
	}
}
