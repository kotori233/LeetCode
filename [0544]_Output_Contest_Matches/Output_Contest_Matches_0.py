class Solution(object):

    def findContestMatch(self, n):
        """
        :type n: int
        :rtype: str
        """
        def helper(groups):
            res = []
            n = len(groups)
            if n == 1:
                return groups
            for i in range(n // 2):
                res.append('(%s,%s)' % (groups[i], groups[n - i - 1]))
            return helper(res)

        return helper(list(range(1, n + 1)))[0]
