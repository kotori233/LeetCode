class Solution(object):

    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        right = num
        left = 0
        while right - left > 1:
            middle = (right + left) // 2
            if middle * middle == num:
                return True
            if middle * middle > num:
                right = middle
            else:
                left = middle
        return False
