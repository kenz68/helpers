def fibonacci(n):
    if n < 0:
        return "Invalid input. Please provide a positive integer."
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_sequence = [0, 1]
        for i in range(2, n+1):
            fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
        return fib_sequence[-1]

def fibonacci_dp(n):
    if n < 2:
        return n
    dp = [0] * n
    dp[0], dp[1] = 0, 1
    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[-1]
    
if __name__ == "__main__":
    # print(fibonacci_dp(0))  # Output: 0
    # print(fibonacci_dp(1))  # Output: 1
    # print(fibonacci_dp(2))  # Output: 1
    # print(fibonacci_dp(3))  # Output: 2
    # print(fibonacci_dp(4))  # Output: 3
    print(fibonacci_dp(10))  # Output: 5
    # Add more test cases as needed
