package main

import "fmt"

func main() {
	fmt.Println(longestCommonPrefix([]string{"flower", "flow", "flight"}))
	fmt.Println(longestCommonPrefix([]string{"dog", "racecar", "car"}))
}

func longestCommonPrefix(strs []string) string {
	var (
		i   int
		res string
	)

	for i = 0; i < len(strs[0]); i++ {
		for _, v := range strs {
			if i == len(v) || v[i] != strs[0][i] {
				return res
			}
		}
		res += string(strs[0][i])
	}
	return res
}
