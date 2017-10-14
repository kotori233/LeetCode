class Solution(object):

    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        import math
        if num < 1:
            return False
        n = int(math.sqrt(num))
        if n * n != num:
            return False
        count = 0
        while n > 0:
            count += (n & 1)
            n >>= 1
        return count == 1
