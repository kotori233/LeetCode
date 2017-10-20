class Solution(object):

    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        while 1:
            n -= i
            if n < 0:
                break
            i += 1
        return i - 1
