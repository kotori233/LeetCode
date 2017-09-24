class Solution(object):

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0 or len(prices) == 1:
            return 0
        price_in = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            price_out = prices[i]
            if price_in > price_out:
                price_in = price_out
            else:
                temp = price_out - price_in
                profit = max(temp, profit)
        return profit
