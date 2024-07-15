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

func main() {
	var arr []*A
	for i := 1; i <= 10; i++ {
		arr = append(arr, &A{a: i, s: ""})
	}
	print(arr)

}
