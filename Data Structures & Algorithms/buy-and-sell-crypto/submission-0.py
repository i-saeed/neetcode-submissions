class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        if len(prices) < 2:
            return profit
        l = 0
        r = 1
        while l < len(prices) - 1:
            profit = max(profit, prices[r] - prices[l])

            if prices[r] < prices[l]:
                l = r

            if r < len(prices) - 1:
                r += 1
            else:
                l += 1

        return profit       