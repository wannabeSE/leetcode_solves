package main

import "fmt"

func main() {
	fmt.Println(sortColors([]int{2, 0, 2, 1, 1, 0}))
	fmt.Println(sortColors([]int{2, 0, 1}))
}

func filler(nums []int, s int, e int, ele int) []int {
	for i := s; i < e; i++ {
		nums[i] = ele
	}
	return nums
}
func sortColors(nums []int) []int {
	var f []int = make([]int, 3)
	for _, v := range nums {
		f[v] += 1
	}
	r, w, _ := f[0], f[1], f[2]
	filler(nums, 0, r, 0)
	filler(nums, r, r+w, 1)
	filler(nums, r+w, len(nums), 2)

	return nums
}
