"""
Problem: Valid Anagram
Question: Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false. Two strings are anagrams if they contain the same characters, with each character appearing the same number of times, regardless of order.

Examples:
    Input: s = "racecar", t = "carrace"  ->  Output: True
    Input: s = "jar", t = "jam"  ->  Output: False
    Input: s = "x", t = "x"  ->  Output: True

Time Complexity: O(s + t)
Space Complexity: O(s + t)
"""


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)

    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False

    return True


if __name__ == "__main__":
    # Test cases
    print(is_anagram("racecar", "carrace"))  # Output: True
    print(is_anagram("jar", "jam"))  # Output: False
    print(is_anagram("x", "x"))  # Output: True

    # Verifications
    assert is_anagram("racecar", "carrace") is True
    assert is_anagram("jar", "jam") is False
    assert is_anagram("x", "x") is True
    print("All tests passed!")
