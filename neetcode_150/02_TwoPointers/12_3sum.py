"""
Problem: 3Sum
Question: Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

Examples:
    Input: nums = [-1, 0, 1, 2, -1, -4]  ->  Output: [[-1, -1, 2], [-1, 0, 1]]
    Explanation:
    nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
    nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
    nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
    The distinct triplets are [-1, 0, 1] and [-1, -1, 2].

    Input: nums = [0, 1, 1]  ->  Output: []
    Explanation: The only possible triplet does not sum up to 0.

    Input: nums = [0, 0, 0]  ->  Output: [[0, 0, 0]]
    Explanation: The only possible triplet sums up to 0.

Constraints:
    3 <= len(nums) <= 3000
    -10^5 <= nums[i] <= 10^5

Time Complexity: O(n^2)
Space Complexity: O(1) or O(n) depending on the sorting implementation
"""


def three_sum(nums: list[int]) -> list[list[int]]:
    # TODO: Implement solution
    pass


if __name__ == "__main__":

    def normalize(triplets: list[list[int]]) -> list[list[int]]:
        return sorted([sorted(t) for t in triplets]) if triplets else []

    # Test cases
    print(three_sum([-1, 0, 1, 2, -1, -4]))  # Expected: [[-1, -1, 2], [-1, 0, 1]]
    print(three_sum([0, 1, 1]))  # Expected: []
    print(three_sum([0, 0, 0]))  # Expected: [[0, 0, 0]]

    # Verifications
    assert normalize(three_sum([-1, 0, 1, 2, -1, -4])) == normalize(
        [[-1, -1, 2], [-1, 0, 1]]
    )
    assert normalize(three_sum([0, 1, 1])) == normalize([])
    assert normalize(three_sum([0, 0, 0])) == normalize([[0, 0, 0]])
    print("All tests passed!")
