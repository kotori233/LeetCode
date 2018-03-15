class Solution(object):

    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        res = n
        for i in range(n // 2, 1, -1):
            if not n % i:
                res = min(res, self.minSteps(n // i) + i)
        return res
