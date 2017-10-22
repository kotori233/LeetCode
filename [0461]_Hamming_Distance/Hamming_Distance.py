class Solution(object):

    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        res = 0
        temp = x ^ y
        while temp:
            res += (temp & 1)
            temp >>= 1
        return res
