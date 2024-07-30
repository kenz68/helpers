package main

import (
	"math"
)

func nearestSumOptimized(numbers []int, target int) []int {
	// Initialize DP table
	dp := make([][]int, len(numbers)+1)
	for i := range dp {
		dp[i] = make([]int, target+1)
		for j := range dp[i] {
			dp[i][j] = math.MaxInt32 // Represents infinity initially
		}
	}
	dp[0][0] = 0 // Base case: empty subset has sum 0

	// Build the DP table
	for i := 1; i <= len(numbers); i++ {
		for j := 0; j <= target; j++ {
			// Exclude the current number
			dp[i][j] = dp[i-1][j]

			// Include if possible
			if j >= numbers[i-1] {
				dp[i][j] = min(dp[i][j], dp[i-1][j-numbers[i-1]]+numbers[i-1])
			}
		}
	}

	// Find the minimum sum greater than or equal to target
	bestSum := math.MaxInt32
	for j := target; j <= target+1; j++ {
		if dp[len(numbers)][j] != math.MaxInt32 && dp[len(numbers)][j] < bestSum {
			bestSum = dp[len(numbers)][j]
		}
	}

	// Backtrack to find the subset
	if bestSum == math.MaxInt32 {
		return nil // No solution found
	}

	var subset []int
	i, j := len(numbers), bestSum
	for i > 0 && j > 0 {
		if dp[i][j] != dp[i-1][j] {
			subset = append(subset, numbers[i-1])
			j -= numbers[i-1]
		}
		i--
	}

	return subset
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

type A struct {
	a int
	s string
}

type orderReq struct {
	Amount struct {
		Value    string `json:"value"`
		Currency string `json:"currency"`
	} `json:"amount"`
	Capture      bool `json:"capture"`
	Confirmation struct {
		Type      string `json:"type"`
		ReturnUrl string `json:"return_url"`
	} `json:"confirmation"`
	Description string `json:"description"`
}

func main() {
	var arr []*A
	for i := 1; i <= 10; i++ {
		arr = append(arr, &A{a: i, s: ""})
	}
	print(arr)

	Description := "Оплата заказа №72"
	obj := orderReq{
		Amount: struct {
			Value    string `json:"value"`
			Currency string `json:"currency"`
		}{
			Value:    "100.00",
			Currency: "RUB",
		},
		Capture: true,
		Confirmation: struct {
			Type      string `json:"type"`
			ReturnUrl string `json:"return_url"`
		}{
			Type:      "redirect",
			ReturnUrl: "https://au.ru/payment/yookassacb",
		},
		Description: Description,
	}

	print(obj)

}
