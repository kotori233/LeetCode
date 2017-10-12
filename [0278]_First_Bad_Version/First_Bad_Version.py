# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution(object):

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        left, right = 1, n
        while right > left:
            middle = (left + right) // 2
            if isBadVersion(middle) is True:
                right = middle
            else:
                left = middle + 1
        return left
