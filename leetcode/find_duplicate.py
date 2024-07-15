from typing import List


def findDuplicates(nums: List[int]) -> List[int]:
    n_dict = {}
    for n in nums:
        n_dict[n] = n_dict[n] + 1 if n in n_dict else 1
    
    result = []
    for k, v in n_dict.items():
         if v > 1: result.append(k)
    return result

nums = [4, 3,2,7,8,2,3,1]
o = findDuplicates(nums)
print(o)