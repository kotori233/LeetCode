class Solution(object):

    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0 for i in range(n + 1)] for j in range(n + 1)]
        for end in range(2, n + 1):
            for start in range(end - 1, 0, -1):
                global_min = float('inf')
                for k in range(start + 1, end):
                    local_max = k + max(dp[start][k - 1], dp[k + 1][end])
                    global_min = min(global_min, local_max)
                if start + 1 == end:
                    dp[start][end] = start
                else:
                    dp[start][end] = global_min
        return dp[1][n]
