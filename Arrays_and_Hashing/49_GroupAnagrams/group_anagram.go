package main

import (
	"fmt"
)

func main() {
	fmt.Println(groupAnagram([]string{"eat", "tea", "tan", "ate", "nat", "bat"}))
}

func groupAnagram(strs []string) [][]string {
	var (
		key      string
		anagram  map[string][]string = make(map[string][]string, 0)
		alphabet [26]int
		ans      [][]string = make([][]string, 0, len(anagram))
	)
	for _, v := range strs {
		for _, ele := range v {
			alphabet[ele-'a']++
		}
		key = fmt.Sprint(alphabet)
		anagram[key] = append(anagram[key], v)
		alphabet = [26]int{}
	}
	for _, val := range anagram {
		ans = append(ans, val)
	}
	return ans
}
