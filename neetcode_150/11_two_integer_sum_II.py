"""
Problem: Two Integer Sum II
Question: Given an array of integers numbers that is sorted in non-decreasing order.
Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.
There will always be exactly one valid solution.
Your solution must use O(1) additional space.

Examples:
    Input: numbers = [1, 2, 3, 4], target = 3  ->  Output: [1, 2]
    Explanation: The sum of 1 and 2 is 3. Since we are assuming a 1-indexed array, index1 = 1, index2 = 2. We return [1, 2].

Constraints:
    2 <= len(numbers) <= 30,000
    -1000 <= numbers[i] <= 1000
    -1000 <= target <= 1000

Time Complexity: O(n)
Space Complexity: O(1)
"""


def two_sum(numbers: list[int], target: int) -> list[int]:
    i, j = 0, len(numbers) - 1
    while i < j:
        current_sum = numbers[i] + numbers[j]
        if current_sum == target:
            return [i + 1, j + 1]
        elif current_sum > target:
            j -= 1
        else:
            i += 1
    return []


if __name__ == "__main__":
    # Test cases
    print(two_sum([1, 2, 3, 4], 3))  # Expected: [1, 2]
    print(two_sum([2, 7, 11, 15], 9))  # Expected: [1, 2]
    print(two_sum([2, 3, 4], 6))  # Expected: [1, 3]
    print(two_sum([-1, 0], -1))  # Expected: [1, 2]

    # Verifications
    assert two_sum([1, 2, 3, 4], 3) == [1, 2]
    assert two_sum([2, 7, 11, 15], 9) == [1, 2]
    assert two_sum([2, 3, 4], 6) == [1, 3]
    assert two_sum([-1, 0], -1) == [1, 2]
    print("All tests passed!")
