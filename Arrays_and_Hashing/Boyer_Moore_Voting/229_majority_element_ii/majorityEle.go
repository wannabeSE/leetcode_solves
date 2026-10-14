package main

import "fmt"

// using Moore voting algo but for two elements
func majorityElement(nums []int) []int {
	// why only two elements can be the highest ?
	// because an element should occur more than n/3 times to be majority element
	// if we calculate there won't be enough space to accommodate more than two elements

	ele1, ele2, count1, count2 := 0, 0, 0, 0
	ans := make([]int, 0, 2)
	for i := range nums {
		if nums[i] == ele1 {
			count1++
		} else if nums[i] == ele2 {
			count2++
			// count1 is assigned for ele1 so it should not overwritten
			// by any other element that is not ele1
			// same logic goes for ele2
		} else if count1 == 0 && nums[i] != ele2 {
			count1 = 1
			ele1 = nums[i]
		} else if count2 == 0 && nums[i] != ele1 {
			count2 = 1
			ele2 = nums[i]
		} else {
			count1--
			count2--
		}
	}
	count1, count2 = 0, 0
	for _, v := range nums {
		switch v {
		case ele1:
			count1++
		case ele2:
			count2++
		}
	}
	if count1 > len(nums)/3 {
		ans = append(ans, ele1)
	}
	if count2 > len(nums)/3 {
		ans = append(ans, ele2)
	}
	return ans
}
func main() {
	cases := [][]int{{3, 2, 3}, {1}, {1, 2}}
	for _, c := range cases {
		fmt.Println(majorityElement(c))
	}
}
