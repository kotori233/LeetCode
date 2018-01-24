class Solution(object):

    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        dp = [[[0 for y in range(n)] for x in range(m)] for k in range(N + 1)]
        for k in range(1, N + 1):
            for x in range(m):
                for y in range(n):
                    t1 = dp[k - 1][x - 1][y] if x else 1
                    t2 = dp[k - 1][x + 1][y] if x != m - 1 else 1
                    t3 = dp[k - 1][x][y - 1] if y else 1
                    t4 = dp[k - 1][x][y + 1] if y != n - 1 else 1
                    dp[k][x][y] = (t1 + t2 + t3 + t4) % 1000000007
        return dp[N][i][j]
