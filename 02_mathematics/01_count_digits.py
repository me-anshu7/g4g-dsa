"""
Problem: Count Digits
Question: Write a function which takes an integer x as an argument and returns count of digits in this number.

Examples:
    Input: x = 9235  ->  Output: 4
    Input: x = 38    ->  Output: 2
    Input: x = 7     ->  Output: 1

Time Complexity: Theta(d) -> where 'd' is the number of digits
Space Complexity: O(1)
"""


def count_digits(x: int) -> int:
    if x == 0:
        return 1

    count = 0
    while x > 0:
        count += 1
        x = x // 10
    return count


if __name__ == "__main__":
    # Test cases from notes
    print(count_digits(9235))  # Output: 4
    print(count_digits(38))  # Output: 2
    print(count_digits(7))  # Output: 1

    # Verifications
    assert count_digits(9235) == 4
    assert count_digits(38) == 2
    assert count_digits(7) == 1
    assert count_digits(0) == 1
    print("All tests passed!")
