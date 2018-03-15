from collections import defaultdict


class Solution(object):

    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        dp = defaultdict(lambda: defaultdict(int))
        dp[0][0] = 0
        for i in range(N):
            for j in dp[i]:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + 1)
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + j)
                dp[i + 2][dp[i][j]] = max(dp[i + 2][dp[i][j]], dp[i][j])
        return max(dp[N].values())
