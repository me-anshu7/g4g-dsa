"""
Problem: Best Time to Buy and Sell Stock
Question: You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.
You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.
Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

Examples:
    Input: prices = [10, 1, 5, 6, 7, 1]  ->  Output: 6
    Explanation: Buy prices[1] (price = 1) and sell prices[4] (price = 7), profit = 7 - 1 = 6.

    Input: prices = [10, 8, 7, 5, 2]  ->  Output: 0
    Explanation: No profitable transactions can be made, thus the max profit is 0.

Constraints:
    1 <= len(prices) <= 100
    0 <= prices[i] <= 100

Time Complexity: O(n)
Space Complexity: O(1)
"""


def max_profit(prices: list[int]) -> int:
    l, r = 0, 1  # left=buy, right=sell
    maxP = 0

    while r < len(prices):
        # profitable ?
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxP = max(profit, maxP)
        else:
            l = r
        r += 1
    return maxP


if __name__ == "__main__":
    # Test cases
    print(max_profit([10, 1, 5, 6, 7, 1]))  # Expected: 6
    print(max_profit([10, 8, 7, 5, 2]))  # Expected: 0
    print(max_profit([7, 1, 5, 3, 6, 4]))  # Expected: 5
    print(max_profit([1]))  # Expected: 0

    # Verifications
    assert max_profit([10, 1, 5, 6, 7, 1]) == 6
    assert max_profit([10, 8, 7, 5, 2]) == 0
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit([1]) == 0
    print("All tests passed!")
