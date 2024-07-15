def countGoodSubstrings(s: str) -> int:
    return sum(len(set(s[i:i+3])) == 3 for i in range(len(s) - 2))


s = "xyzzaz"
print(countGoodSubstrings(s))
