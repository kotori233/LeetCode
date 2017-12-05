class Solution(object):

    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        if n == 1:
            return 10
        ans, res = 9, 10
        for i in range(2, n + 1):
            if i > 10:
                return res
            ans *= (11 - i)
            res += ans
        return res
