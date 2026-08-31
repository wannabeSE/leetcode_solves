package main

import (
	"fmt"
	"slices"
)

func main() {
	fmt.Println(topKFrequent([]int{1, 1, 1, 2, 2, 3}, 2))
	fmt.Println(topKFrequent([]int{1}, 1))
}

func topKFrequent(nums []int, k int) []int {
	var (
		bucket [][]int     = make([][]int, len(nums)+1)
		freq   map[int]int = make(map[int]int, len(nums))
		ans    []int       = make([]int, 0, k)
	)
	for _, v := range nums {
		freq[v]++
	}
	for key, val := range freq {
		bucket[val] = append(bucket[val], key)
	}

	for _, ele := range slices.Backward(bucket) {
		if len(ans) == k {
			return ans
		}
		ans = append(ans, ele...)
	}
	return ans
}
