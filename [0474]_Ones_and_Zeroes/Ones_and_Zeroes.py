class Solution(object):

    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
        for each in strs:
            count0 = each.count('0')
            count1 = len(each) - count0
            for i in range(m, count0 - 1, -1):
                for j in range(n, count1 - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - count0][j - count1] + 1)
        return dp[m][n]
