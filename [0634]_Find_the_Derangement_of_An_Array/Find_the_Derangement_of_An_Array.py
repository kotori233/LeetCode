class Solution(object):

    def findDerangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        dp = [0 for i in range(n + 1)]
        dp[2] = 1
        for i in range(3, n + 1):
            dp[i] = (i - 1) * (dp[i - 1] + dp[i - 2]) % 1000000007
        return dp[n]
