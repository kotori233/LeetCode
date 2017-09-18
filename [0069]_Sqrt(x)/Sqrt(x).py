class Solution(object):

    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1 or x == 0:
            return x
        right = x
        left = 0
        while right - left > 1:
            middle = (right + left) // 2
            if middle * middle == x:
                return middle
            if middle * middle > x:
                right = middle
            else:
                left = middle
        return left
