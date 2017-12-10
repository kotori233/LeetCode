class Solution(object):

    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        if n == 0:
            return 0
        total = sum(A)
        dp = [0 for i in range(n)]
        dp[0] = sum([i * A[i] for i in range(n)])
        for i in range(1, n):
            dp[i] = dp[i - 1] + total - n * A[n - i]
        return max(dp)
