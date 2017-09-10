class Solution(object):

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 0:
            x = int(str(x)[::-1])
        else:
            x = -int(str(-x)[::-1])
        if x > 2147483647 or x <= -2147483648:
            return 0
        else:
            return x
