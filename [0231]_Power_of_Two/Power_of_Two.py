class Solution(object):

    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        count = 0
        while n > 0:
            count += (n & 1)
            n >>= 1
        return count == 1
