class Solution(object):

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        flag = (dividend < 0) ^ (divisor < 0)
        a = abs(dividend)
        b = abs(divisor)
        count = 0
        while a >= b:
            c = b
            each = 1
            while a >= c:
                a -= c
                count += each
                c <<= 1
                each <<= 1
        if flag:
            return max(-2147483648, -count)
        return min(0x7FFFFFFF, count)
