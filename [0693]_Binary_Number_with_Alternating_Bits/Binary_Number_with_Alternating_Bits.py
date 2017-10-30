class Solution(object):

    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        pre = None
        while n:
            temp = n & 1
            if pre is not None and pre ^ temp == 0:
                return False
            pre = temp
            n >>= 1
        return True
