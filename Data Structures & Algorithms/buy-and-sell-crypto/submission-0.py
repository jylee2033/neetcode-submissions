class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 0
        lowest = prices[0]

        for price in prices:
            lowest = min(lowest, price)
            m = max(m, price - lowest)

        return m