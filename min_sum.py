def nearest_sum_optimized(numbers, target):
    """Finds the subset of numbers from 'numbers' that has the minimum sum 
       greater than or equal to 'target'.

    Args:
        numbers: A list of integers.
        target: The target sum.

    Returns:
        A list containing the elements of the subset with the closest sum, 
        or None if no subset is found.
    """

    dp = [[float('inf')] * (target + 1) for _ in range(len(numbers) + 1)]
    dp[0][0] = 0  # Base case: An empty subset has a sum of 0

    # Iterate over the numbers and build the DP table.
    for i in range(1, len(numbers) + 1):
        for j in range(target + 1):
            # Exclude the current number.
            dp[i][j] = dp[i - 1][j]

            # Include the current number if it doesn't exceed the current 'j'.
            if j >= numbers[i - 1]:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - numbers[i - 1]] + numbers[i - 1])

    # Find the smallest sum greater than or equal to the target.
    best_sum = float('inf')
    for j in range(target, target + 1):
        if dp[len(numbers)][j] != float('inf') and dp[len(numbers)][j] < best_sum:
            best_sum = dp[len(numbers)][j] 

    # Backtrack to find the actual subset.
    if best_sum == float('inf'):
        return None  # No solution found

    subset = []
    i, j = len(numbers), best_sum
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:  # Value was included in this sum
            subset.append(numbers[i - 1])
            j -= numbers[i - 1]
        i -= 1

    return subset

# Example usage
numbers = [1, 1, 2, 3, 5, 6, 8, 10]
target = 8

subset = nearest_sum_optimized(numbers, target)

if subset:
    print(f"Subset with the closest sum (larger or equal to {target}): {subset}")
else:
    print(f"No subset found with a sum close to {target}")
