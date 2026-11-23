"""
Problem: Valid Palindrome
Question: Given a string s, return true if it is a palindrome, otherwise return false.
A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.
Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Examples:
    Input: s = "Was it a car or a cat I saw?"  ->  Output: True
    Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

    Input: s = "tab a cat"  ->  Output: False
    Explanation: "tabacat" is not a palindrome.

Constraints:
    1 <= len(s) <= 1000
    s is made up of only printable ASCII characters.

Time Complexity: O(n)
Space Complexity: O(1) with two pointers (or O(n) if creating a filtered string)
"""


def is_palindrome(s: str) -> bool:
    # TODO: Implement solution
    pass


if __name__ == "__main__":
    # Test cases
    print(is_palindrome("Was it a car or a cat I saw?"))  # Expected: True
    print(is_palindrome("tab a cat"))  # Expected: False
    print(is_palindrome(" "))  # Expected: True (empty string after filtering)
    print(is_palindrome("0P"))  # Expected: False

    # Verifications
    assert is_palindrome("Was it a car or a cat I saw?") is True
    assert is_palindrome("tab a cat") is False
    assert is_palindrome(" ") is True
    assert is_palindrome("0P") is False
    print("All tests passed!")
