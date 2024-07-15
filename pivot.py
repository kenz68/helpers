from typing import List


def pivotIndex(nums: List[int]) -> int:
    for index in range(len(nums)):
        if sum(nums[:index]) == sum(nums[index+1:]):
            return index
    return -1


nums = [1, 7, 3, 6, 5, 6]
print(pivotIndex(nums))
print(pivotIndex([1, 2, 3]))