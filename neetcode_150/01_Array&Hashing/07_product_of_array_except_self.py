"""
Problem: Products of Array Except Self
Question: Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(n) time without using the division operation?

Examples:
    Input: nums = [1, 2, 4, 6]  ->  Output: [48, 24, 12, 8]
    Input: nums = [-1, 0, 1, 2, 3]  ->  Output: [0, -6, 0, 0, 0]

Constraints:
    2 <= nums.length <= 100,000
    -30 <= nums[i] <= 30
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Time Complexity: O(n)
Space Complexity: O(1) auxiliary space (excluding the output array)
"""


def product_except_self(nums: list[int]) -> list[int]:
    res = [1] * len(nums)
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
    postfix = 1
    for j in range(len(nums) - 1, -1, -1):
        res[j] *= postfix
        postfix *= nums[j]
    return res


if __name__ == "__main__":
    # Test cases
    print(product_except_self([1, 2, 4, 6]))  # Expected: [48, 24, 12, 8]
    print(product_except_self([-1, 0, 1, 2, 3]))  # Expected: [0, -6, 0, 0, 0]

    # Verifications
    assert product_except_self([1, 2, 4, 6]) == [48, 24, 12, 8]
    assert product_except_self([-1, 0, 1, 2, 3]) == [0, -6, 0, 0, 0]
    print("All tests passed!")
