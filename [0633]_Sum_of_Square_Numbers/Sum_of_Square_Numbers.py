class Solution(object):

    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        m = int((c // 2) ** 0.5)
        while m > -1:
            d = c - m * m
            if int(d ** 0.5) ** 2 == d:
                return True
            m -= 1
        return False
