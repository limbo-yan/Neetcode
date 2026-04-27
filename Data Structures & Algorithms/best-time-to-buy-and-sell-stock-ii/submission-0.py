class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyin = prices[0]
        profit = 0
        for price in prices:
            if price > buyin:
                profit += price - buyin
            buyin = price
        return profit
        