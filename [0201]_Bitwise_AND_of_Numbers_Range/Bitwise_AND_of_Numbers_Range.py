class Solution(object):

    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        d = 0xFFFFFFFF
        while (m & d) != (n & d):
            d <<= 1
        return m & d
