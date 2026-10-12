package main

import "fmt"

func maxProfit(prices []int) int {
	buy, sell, profit := 0, 1, 0
	bought := false
	for sell < len(prices) {
		// cannot buy if the selling price is lesser than the buying price
		// this part won't be executed
		// if the selling price is not less than buying price
		// so till then we have not bought any stock yet
		if prices[sell] < prices[buy] {
			// so we buy at the lowest price
			buy = sell
		} else {
			// as the buying price is lesser than the selling price
			// now we buy the stock
			bought = true
			// we should sell the stock
			// if we can buy the stock again at lesser price the next day
			// so that we can make more profit
			if sell+1 < len(prices) && prices[sell] >= prices[sell+1] {
				// before buying we should store the current profit
				profit += prices[sell] - prices[buy]
				// buying the stock at lesser price
				buy = sell + 1
				// we do not want 'buy' and 'sell' to be at the same position
				sell++
			}
		}
		sell++
	}
	// we bought the stocks but did not sell to make profit
	// as there was no lesser price
	// than the first time or the last time we bought the stock at.
	if bought {
		// adding the profit with the profit we made so far
		// or it might be first time we are selling our stocks
		// cause we might haven't been able to buy the stocks more than once.
		profit += prices[sell-1] - prices[buy]
	}
	return profit
}
func main() {
	cases := [][]int{{7, 1, 5, 3, 6, 4}, {1, 2, 3, 4, 5}, {7, 6, 4, 3, 1}, {2, 1, 4}, {6, 1, 3, 2, 4, 7}}
	for _, c := range cases {
		fmt.Println(maxProfit(c))
	}
}
