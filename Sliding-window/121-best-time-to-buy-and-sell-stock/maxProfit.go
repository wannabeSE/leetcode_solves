package main

import "fmt"

func maxProfit(prices []int) int {
	buy, sell, profit := 0, 1, 0
	//since sell is the only pointer we are incrementing
	for sell < len(prices) {
		if prices[buy] > prices[sell] {
			// if the buying price is greater than the selling price
			// that means the current selling price is very low on that particular day
			// so we should buy on that day to maximize the profit
			buy = sell
		} else {
			profit = max(profit, prices[sell]-prices[buy])
		}
		// no matter what the 'sell' pointer should be always incremented
		// as we are looking forward to maximize the profit
		sell++

	}
	return profit
}
func main() {
	cases := [][]int{{2, 1, 4}, {7, 1, 5, 3, 6, 4}, {7, 6, 4, 3, 1}, {2, 1, 2, 1, 0, 1, 2}}
	for _, c := range cases {
		fmt.Println(maxProfit(c))
	}
}
