class Solution(object):

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 or n == 2:
            return n
        step = [1] * (n + 1)
        for i in range(2, n + 1):
            step[i] = step[i - 1] + step[i - 2]
        return step[n]
