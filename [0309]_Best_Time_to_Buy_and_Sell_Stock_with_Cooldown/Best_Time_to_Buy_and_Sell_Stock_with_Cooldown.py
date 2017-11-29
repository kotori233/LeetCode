class Solution(object):

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        free, have, cool = 0, float('-inf'), float('-inf')
        for i in prices:
            free, have, cool = max(free, cool), max(have, free - i), have + i
        return max(free, cool)
