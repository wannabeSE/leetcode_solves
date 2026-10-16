package main

import (
	"fmt"
	"strings"
)

func mergeAlternately(word1 string, word2 string) string {
	wp1, wp2 := 0, 0
	var ans strings.Builder
	n := len(word1) + len(word2)
	for i := range n {
		if wp1 < len(word1) && i%2 == 0 {
			ans.WriteByte(word1[wp1])
			wp1++
		} else if wp2 < len(word2) && i%2 != 0 {
			ans.WriteByte(word2[wp2])
			wp2++
		} else if wp1 < len(word1) {
			ans.WriteByte(word1[wp1])
			wp1++
		} else {
			ans.WriteByte(word2[wp2])
			wp2++
		}
	}
	return ans.String()
}
func main() {
	fmt.Println(mergeAlternately("ab", "pqrs"))
	fmt.Println(mergeAlternately("abcd", "pq"))
}
