"""
Problem: Encode and Decode Strings
Question: Design an algorithm to encode a list of strings to a single string.
The encoded string is then sent over the network and decoded back to the original list of strings.

Machine 1 (sender) does:
    encoded_string = encode(strs)

Machine 2 (receiver) does:
    decoded_strs = decode(encoded_string)

decoded_strs should be identical to the original strs.

Examples:
    Input: strs = ["Hello", "World"]  ->  Output: ["Hello", "World"]
    Input: strs = [""]  ->  Output: [""]
    Input: strs = []  ->  Output: []

Constraints:
    0 <= len(strs) < 100
    0 <= len(strs[i]) < 200
    strs[i] contains any possible characters out of 256 valid ASCII characters.

Time Complexity: O(N) where N is the total number of characters across all strings
Space Complexity: O(N) to store the encoded string / decoded list
"""


def encode(strs: list[str]) -> str:
    encoded_str = "".join(f"{len(s)}#{s}" for s in strs)
    print(encoded_str)
    return encoded_str


def decode(s: str) -> list[str]:
    decoded_list = []
    i = 0
    while i < len(s):
        # 1. Find the index of the delimiter '#' starting from i
        j = i
        while s[j] != "#":
            j += 1

        # 2. Extract the length (handles multi-digit lengths like 10#, 123#, etc.)
        length = int(s[i:j])

        # 3. Define the start and end boundaries for the actual string
        start = j + 1
        end = start + length

        # 4. Extract the string and add it to our list
        decoded_list.append(s[start:end])

        # 5. Move i forward to the start of the next length prefix
        i = end

    return decoded_list


if __name__ == "__main__":
    # Test cases
    test_1 = ["Hello", "World"]
    test_2 = [""]
    test_3 = []
    test_4 = ["neet", "code", "love", "you"]
    test_5 = ["we", "say", ":", "yes", "!@#$%^&*()"]
    test_6 = ["#", "##", "1#", "2#3#"]

    print("Encoded test_1:", encode(test_1))
    print("Decoded test_1:", decode(encode(test_1)))

    # Verifications
    assert decode(encode(test_1)) == test_1
    assert decode(encode(test_2)) == test_2
    assert decode(encode(test_3)) == test_3
    assert decode(encode(test_4)) == test_4
    assert decode(encode(test_5)) == test_5
    assert decode(encode(test_6)) == test_6
    print("All tests passed!")
