"""
Problem: Contains Duplicate
Question: Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Examples:
    Input: nums = [1, 2, 3, 1]  ->  Output: True
    Input: nums = [1, 2, 3, 4]  ->  Output: False
    Input: nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]  ->  Output: True

Time Complexity: O(n)
Space Complexity: O(n)
"""


def contains_duplicate(nums: list[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


if __name__ == "__main__":
    # Test cases
    print(contains_duplicate([1, 2, 3, 1]))  # Output: True
    print(contains_duplicate([1, 2, 3, 4]))  # Output: False
    print(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # Output: True

    # Verifications
    assert contains_duplicate([1, 2, 3, 1]) is True
    assert contains_duplicate([1, 2, 3, 4]) is False
    assert contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True
    print("All tests passed!")
