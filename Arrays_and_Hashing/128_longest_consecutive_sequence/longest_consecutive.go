package main

import "fmt"

func main() {
	fmt.Println(longestConsecutive([]int{100, 4, 200, 1, 3, 2}))
	fmt.Println(longestConsecutive([]int{0, 3, 7, 2, 5, 8, 4, 6, 0, 1}))
	fmt.Println(longestConsecutive([]int{}))
}

func longestConsecutive(nums []int) int {
	var (
		longest int             = 0
		set     map[int]struct{} = make(map[int]struct{}, 0)
	)
	if len(nums) == 0 {
		return 0
	}
	for _, v := range nums {
		set[v] = struct{}{}
	}
	for k := range set {
		_, prev := set[k-1]
		if prev == false {
			length := 0
			for {
				if _, present := set[k+length]; !present {
					break
				}
				length++
			}
			longest = max(longest, length)
		}
	}
	return longest
}
