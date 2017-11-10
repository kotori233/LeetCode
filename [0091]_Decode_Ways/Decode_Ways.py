class Solution(object):

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '' or s[0] == '0':
            return 0
        n = len(s)
        dp = [0 for i in range(n + 1)]
        dp[0] = dp[1] = 1
        for i in range(1, n):
            if s[i] == '0' and s[i - 1] not in '12':
                return 0
            if s[i] != '0':
                dp[i + 1] += dp[i]
            if s[i - 1] == '1' or (s[i - 1] == '2' and s[i] in '0123456'):
                dp[i + 1] += dp[i - 1]
        return dp[n]
