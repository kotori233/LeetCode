class Solution(object):

    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while b != 0:
            carry = a & b
            a = (a ^ b) % 0x100000000
            b = (carry << 1) % 0x100000000
        if a <= 0x7FFFFFFF:
            return a
        else:
            return a | (~ 0x100000000 + 1)
