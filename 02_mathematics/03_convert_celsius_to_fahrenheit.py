"""
Problem: Convert Celsius To Fahrenheit
Question: Given a temperature in celsius C. You need to convert the given temperature into Fahrenheit.

Examples:
    Input: C = 32  ->  Output: 89.6   Explanation: Using the conversion formula of celsius to fahrenheit, it can be calculated that, for 32 degree celsius, the temperature in Fahrenheit = 89.6
    Input: C = 50  ->  Output: 122.0  Explanation: Using the conversion formula of celsius to fahrenheit, it can be calculated that, for 50 degree celsius, the temperature in Fahrenheit = 122.0

    Formula:
        F = (C * 9/5) + 32

Time Complexity: Theta(1)
Space Complexity: O(1)
"""


def convert_celsius_to_fahrenheit(C: int) -> float:
    return (C * 9 / 5) + 32


if __name__ == "__main__":
    # Test cases from notes
    print(convert_celsius_to_fahrenheit(32))  # Output: 89.6
    print(convert_celsius_to_fahrenheit(50))  # Output: 122.0

    # Verifications
    assert convert_celsius_to_fahrenheit(32) == 89.6
    assert convert_celsius_to_fahrenheit(50) == 122.0
    print("All tests passed!")
