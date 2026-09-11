"""
Problem: Quadratic Equation Roots
Question: Given a quadratic equation ax^2 + bx + c = 0, find its roots. If the equation has real roots, then return floor value of each root in decreasing order, If the roots are imaginary return -1, the driver code will print Imaginary

Examples:
    Input: a = 1, b = -2, c = 1
    Output: [1, 1]
    Explanation: The roots of the equation are 1 and 1.

    Input: a = 1, b = -7, c = 12
    Output: [4, 3]
    Explanation: The roots of the equation are 4 and 3.

Time Complexity: O(1)
Space Complexity: O(1)
"""
import math


def quadratic_roots(a: int, b: int, c: int) -> list[int]:
    # Calculate the discriminant
    delta = b**2 - 4 * a * c

    # If discriminant is negative, the roots are imaginary
    if delta < 0:
        return [-1]

    # Calculate the roots
    sqrt_delta = math.sqrt(delta)
    root1 = math.floor((-b + sqrt_delta) / (2 * a))
    root2 = math.floor((-b - sqrt_delta) / (2 * a))

    # Return the roots in decreasing order
    return [max(root1, root2), min(root1, root2)]


if __name__ == "__main__":
    # Test cases from notes
    print(quadratic_roots(1, -2, 1))   # Output: [1, 1]
    print(quadratic_roots(1, -7, 12))  # Output: [4, 3]
    print(quadratic_roots(1, 4, 8))    # Output: [-1] (Imaginary)

    # Verifications
    assert quadratic_roots(1, -2, 1) == [1, 1]
    assert quadratic_roots(1, -7, 12) == [4, 3]
    assert quadratic_roots(1, 4, 8) == [-1]
    print("All tests passed!")