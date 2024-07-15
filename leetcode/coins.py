
def coinChange(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    r = 0
    coins = sorted(coins, reverse=True)
    for c in coins:
        m = amount % c
        if m == 0:
            r += amount/c
            return r
        if m > 0 and amount >= c:
            r += amount//c
            amount %= c
    if amount == 0:
        return r
    if len(coins) == 0:
        return -1
    return coinChange(coins[1:], amount)
# c = [1, 2, 5]
# a = 11
# r = coinChange(c, a)
# print(r)
# print(coinChange([2], 3))
print(coinChange([186,419,83,408], 6249))