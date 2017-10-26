class Solution(object):

    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        kinds = len(set(candies))
        n = len(candies)
        return min(kinds, n // 2)
