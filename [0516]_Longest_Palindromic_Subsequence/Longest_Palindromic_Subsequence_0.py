class Solution(object):

    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [0 for i in range(n)]
        for i in range(n - 1, -1, -1):
            new = dp[:]
            new[i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    new[j] = dp[j - 1] + 2
                else:
                    new[j] = max(dp[j], new[j - 1])
            dp = new
        return dp[n - 1]
