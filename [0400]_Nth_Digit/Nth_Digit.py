class Solution(object):

    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 10:
            return n
        digit = -1
        while n >= 0:
            digit += 1
            temp = n
            n -= 9 * (10 ** digit) * (digit + 1)
        res = (temp - 1) // (digit + 1) + 10 ** digit
        pos = temp % (digit + 1) - 1
        if pos == -1:
            pos = digit
        return int(str(res)[pos])
