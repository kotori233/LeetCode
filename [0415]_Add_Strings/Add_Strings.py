class Solution(object):

    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = ''
        d1, d2 = len(num1), len(num2)
        carry = 0
        while d1 or d2 or carry:
            if d1 > 0:
                d1 -= 1
                digit = int(num1[d1])
            else:
                digit = 0
            if d2 > 0:
                d2 -= 1
                digit += int(num2[d2])
            digit += carry
            if digit > 9:
                carry = 1
            else:
                carry = 0
            res = str(digit % 10) + res
        return res
