"""
Problem: Two Sum
Question: Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j. You may assume that every input has exactly one pair of indices i and j that satisfy the condition. Return the answer with the smaller index first.

Examples:
    Input: nums = [3, 4, 5, 6], target = 7  ->  Output: [0, 1]
    Input: nums = [4, 5, 6], target = 10  ->  Output: [0, 2]
    Input: nums = [5, 5], target = 10  ->  Output: [0, 1]

Time Complexity: O(n)
Space Complexity: O(n)
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return []


if __name__ == "__main__":
    # Test cases
    print(two_sum([3, 4, 5, 6], 7))  # Output: [0, 1]
    print(two_sum([4, 5, 6], 10))  # Output: [0, 2]
    print(two_sum([5, 5], 10))  # Output: [0, 1]

    # Verifications
    assert two_sum([3, 4, 5, 6], 7) == [0, 1]
    assert two_sum([4, 5, 6], 10) == [0, 2]
    assert two_sum([5, 5], 10) == [0, 1]
    print("All tests passed!")
