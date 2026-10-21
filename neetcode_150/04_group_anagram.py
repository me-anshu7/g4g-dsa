"""
Problem: Group Anagrams
Question: Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order. An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Examples:
    Input: strs = ["act", "pots", "tops", "cat", "stop", "hat"]  ->  Output: [["hat"], ["act", "cat"], ["stop", "pots", "tops"]]
    Input: strs = ["x"]  ->  Output: [["x"]]
    Input: strs = [""]  ->  Output: [[""]]

Time Complexity: O(m * n) or O(m * n log n), where m is the number of strings and n is the max length of a string.
Space Complexity: O(m * n)
"""


def group_anagrams(strs: list[str]) -> list[list[str]]:
    grp = {}
    for s in strs:
        sorted_key = "".join(sorted(s))
        if sorted_key not in grp:
            grp[sorted_key] = []
        grp[sorted_key].append(s)
    
    return list(grp.values())


if __name__ == "__main__":
    def normalize(groups: list[list[str]]) -> list[list[str]]:
        return sorted([sorted(group) for group in groups]) if groups else []

    # Test cases
    print(group_anagrams(["act", "pots", "tops", "cat", "stop", "hat"]))
    print(group_anagrams(["x"]))
    print(group_anagrams([""]))

    # Verifications
    assert normalize(group_anagrams(["act", "pots", "tops", "cat", "stop", "hat"])) == normalize(
        [["hat"], ["act", "cat"], ["stop", "pots", "tops"]]
    )
    assert normalize(group_anagrams(["x"])) == normalize([["x"]])
    assert normalize(group_anagrams([""])) == normalize([[""]])
    print("All tests passed!")
