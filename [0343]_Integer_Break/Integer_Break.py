class Solution(object):

    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 4:
            return n - 1
        factor = n // 3
        last = n % 3
        if last == 2:
            return 3 ** factor * 2
        return 3 ** (factor - 1) * (3 + last)
