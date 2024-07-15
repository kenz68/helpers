from typing import List


# def firstMissingPositive(nums: List[int]) -> int:
#     nums = sorted(filter(lambda x: x > 0, set(nums)))
#     r = 1
#     for n in nums:
#         if n > r:
#             return r
#         r += 1
#     return r
def firstMissingPositive(nums: List[int]) -> int:
    """
    Finds the first missing positive integer in a list of numbers.

    Args:
        nums: A list of integers.

    Returns:
        The first missing positive integer.
    """

    num_set = set(nums)  # Create a set for efficient existence checks

    for i in range(1, len(nums) + 2):  # Iterate up to the potential max
        if i not in num_set:
            return i

    return len(nums) + 1  # All numbers from 1 to len(nums) exist


print(firstMissingPositive([1, 2, 0]))
print(firstMissingPositive([3, 4, -1, 1]))
print(firstMissingPositive([7, 8, 9, 11, 12]))
print(firstMissingPositive([1, 1]))
