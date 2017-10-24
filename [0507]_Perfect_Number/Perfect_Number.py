class Solution(object):

    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 2:
            return False
        res = 0
        top = int(num ** 0.5)
        while top:
            if num % top == 0:
                res += (top + num // top)
            top -= 1
        if res == num * 2:
            return True
        return False
