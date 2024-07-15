from typing import List


def sumOfUnique(nums: List[int]) -> int:
    d = {}
    for i in nums:
        d[i] = d[i] + 1 if i in d else 1
    return sum([k for k, v in d.items() if v == 1])


print(sumOfUnique([1, 2, 3, 2]))
