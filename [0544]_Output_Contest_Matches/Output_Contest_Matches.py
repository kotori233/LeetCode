class Solution(object):

    def findContestMatch(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = list(range(1, n + 1))
        while n > 1:
            for i in range(n // 2):
                res[i] = '(%s,%s)' % (res[i], res[n - i - 1])
            n //= 2
        return res[0]
