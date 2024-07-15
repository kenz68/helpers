
def longestIdealString(s: str, k: int) -> int:
    dp = [0] * 128
    for c in s:
        i = ord(c)
        dp[i] = max(dp[i - k: i + k + 1]) + 1
    return max(dp)

s = "acfgbd"
k = 4
r = longestIdealString(s, k)
print(r)
