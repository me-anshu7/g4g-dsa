"""
Problem: Top K Frequent Elements
Question: Given an integer array nums and an integer k, return the k most frequent elements within the array.
The test cases are generated such that the answer is always unique.
You may return the output in any order.

Examples:
    Input: nums = [1, 2, 2, 3, 3, 3], k = 2  ->  Output: [2, 3]
    Input: nums = [7, 7], k = 1  ->  Output: [7]

Constraints:
    1 <= nums.length <= 10^4
    -1000 <= nums[i] <= 1000
    1 <= k <= number of distinct elements in nums

Time Complexity: O(n) with bucket sort or O(n log k) with min-heap
Space Complexity: O(n)
"""

# import heapq
# from collections import Counter


def top_k_frequent(nums: list[int], k: int) -> list[int]:

    # My Solution - O(nlogn)
    count, res = {}, []
    for num in nums:
        count[num] = 1 + count.get(num, 0)

    # print(sorted(count.items(), key=lambda item: item[1], reverse=True))
    count = sorted(count.items(), key=lambda item: item[1], reverse=True)

    res = [num for num, freq in count[:k]]

    return res

    ## Not my solution - O(nlogk)
    # count = Counter(nums)
    # return heapq.nlargest(k, count.keys(), key=count.get)


if __name__ == "__main__":
    # Test cases
    print(top_k_frequent([1, 2, 2, 3, 3, 3], 2))  # Expected: [2, 3] (any order)
    print(top_k_frequent([7, 7], 1))  # Expected: [7]

    # Verifications
    assert sorted(top_k_frequent([1, 2, 2, 3, 3, 3], 2)) == sorted([2, 3])
    assert sorted(top_k_frequent([7, 7], 1)) == sorted([7])
    print("All tests passed!")
