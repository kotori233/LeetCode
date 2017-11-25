class Solution(object):

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        while n % 4 == 0:
            n //= 4
        if n % 8 == 7:
            return 4
        i = 0
        while i * i <= n:
            j = int((n - i * i) ** 0.5)
            if j * j + i * i == n:
                if 0 in (i, j):
                    return 1
                return 2
            i += 1
        return 3
