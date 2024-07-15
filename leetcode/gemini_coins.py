def min_coins(coins, amount):
    """
    This function calculates the minimum number of coins required to make a certain amount using dynamic programming.

    Args:
        coins: A list of coin denominations.
        amount: The target amount to make.

    Returns:
        The minimum number of coins required to make the amount, or -1 if it's impossible.
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    print(f"init dp: {dp}")
    for coin in coins:
        for i in range(coin, amount + 1):
            print(f"dp[{i}] = {dp[i]} vs dp[{i - coin}] + 1 = {dp[i - coin] + 1}")
            dp[i] = min(dp[i], dp[i - coin] + 1)
        print(f"dp {dp}")
    return dp[amount] if dp[amount] != float('inf') else -1

# Example usage
coins = [2, 5, 1]
amount = 11

min_coins_required = min_coins(coins, amount)

if min_coins_required != -1:
    print(f"Minimum number of coins required: {min_coins_required}")
else:
    print("It's impossible to make the target amount with the given coins.")
