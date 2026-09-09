"""
Problem: Absolute Value
Question: You are given an integer n, find the absolute value of the integer n.

Examples:
    Input: n = -32  ->  Output: 32
    Input: n = 45   ->  Output: 45
    Input: n = 0    ->  Output: 0

Time Complexity: Theta(1)
Space Complexity: O(1)
"""


def absolute_value(n: int) -> int:
    if n < 0:
        return -n
    return n


if __name__ == "__main__":
    # Test cases from notes
    print(absolute_value(-32))  # Output: 32
    print(absolute_value(45))  # Output: 45
    print(absolute_value(0))  # Output: 0

    # Verifications
    assert absolute_value(-32) == 32
    assert absolute_value(45) == 45
    assert absolute_value(0) == 0
    print("All tests passed!")
