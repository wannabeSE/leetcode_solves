package main

import "fmt"

type NumArray struct {
	numArr [][]int
}

func Constructor(nums []int) NumArray {
	//creating prefix sum array
	for i := 1; i < len(nums); i++ {
		nums[i] = nums[i-1] + nums[i]
	}
	return NumArray{numArr: [][]int{nums}}
}

func (this *NumArray) SumRange(left int, right int) int {
	if left == 0 {
		return this.numArr[0][right]
	}
	return this.numArr[0][right] - this.numArr[0][left-1]
}

func main() {
	arr := Constructor([]int{-2, 0, 3, -5, 2, -1})
	p1 := arr.SumRange(0, 2)
	p2 := arr.SumRange(2, 5)
	fmt.Println(arr, p1, p2)
}
