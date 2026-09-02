class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1 = prices[0]
        sell1 = 0

        buy2 = prices[0]
        sell2 = 0

        for price in prices:
            buy1 = min(price,buy1)
            sell1 = max(sell1,price-buy1)

            buy2 = min(price-sell1, buy2)
            sell2 = max(sell2,price-buy2)

        return sell2
        