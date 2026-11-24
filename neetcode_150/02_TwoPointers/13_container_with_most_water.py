"""
Problem: Container With Most Water
Question: You are given an integer array heights where heights[i] represents the height of the ith bar.
You may choose any two bars to form a container. Return the maximum amount of water a container can store.

Diagram:
    See `13_container_with_most_water.png` in this directory for the visual diagram.

    Height
      8 |
      7 |      |                   |
      6 |      |~~~~~~~~~~~~~~~~~~~|~~~~~~~~~|   <- Water level = 6
      5 |      |         |         |         |
      4 |      |         |    |    |         |
      3 |      |         |    |    |    |    |
      2 |      |    |    |    |    |    |    |
      1 | |    |    |    |    |    |    |    |
      0 +---------------------------------------
        0    1    2    3    4    5    6    7
        [1,  7,   2,   5,   4,   7,   3,   6]
             ^                               ^
             Left (i=1)                  Right (i=7)
             Width = 7 - 1 = 6, Min Height = min(7, 6) = 6
             Area = 6 * 6 = 36

Examples:
    Input: heights = [1, 7, 2, 5, 4, 7, 3, 6]  ->  Output: 36
    Explanation: The bars at indices 1 and 7 have heights 7 and 6. The container has width 7 - 1 = 6 and height min(7, 6) = 6, so it can store 6 * 6 = 36 units of water. This is the maximum possible area.

    Input: heights = [2, 2, 2]  ->  Output: 4

Constraints:
    2 <= len(heights) <= 100,000
    0 <= heights[i] <= 10,000

Time Complexity: O(n)
Space Complexity: O(1)
"""


def max_area(heights: list[int]) -> int:
    # Explicit guard clause for empty or single-element lists
    if len(heights) < 2:
        return 0

    l, r = 0, len(heights) - 1
    res = 0

    while l < r:
        area = (r - l) * min(heights[l], heights[r])
        res = max(res, area)

        if heights[l] < heights[r]:
            l += 1
        else:
            r -= 1

    return res


if __name__ == "__main__":
    # Test cases
    print(max_area([1, 7, 2, 5, 4, 7, 3, 6]))  # Expected: 36
    print(max_area([2, 2, 2]))  # Expected: 4

    # Verifications
    assert max_area([1, 7, 2, 5, 4, 7, 3, 6]) == 36
    assert max_area([2, 2, 2]) == 4
    print("All tests passed!")
