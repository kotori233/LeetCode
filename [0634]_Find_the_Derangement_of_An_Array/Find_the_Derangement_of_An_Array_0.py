class Solution(object):

    def findDerangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        a, b = 0, 1
        for i in range(3, n + 1):
            a, b = b, (i - 1) * (a + b) % 1000000007
        return b
