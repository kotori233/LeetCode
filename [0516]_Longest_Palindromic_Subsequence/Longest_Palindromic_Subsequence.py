from collections import defaultdict


class Solution(object):

    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        def helper(i, j):
            if j in cache[i]:
                return cache[i][j]
            if i == j:
                return 1
            if i > j:
                return 0
            if s[i] == s[j]:
                cache[i][j] = helper(i + 1, j - 1) + 2
            else:
                cache[i][j] = max(helper(i, j - 1), helper(i + 1, j))
            return cache[i][j]

        cache = defaultdict(dict)
        return helper(0, len(s) - 1)
