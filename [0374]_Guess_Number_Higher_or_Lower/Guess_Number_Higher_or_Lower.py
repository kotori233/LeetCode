# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):


class Solution(object):

    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        left, right = 1, n
        while right > left:
            middle = (left + right) // 2
            res = guess(middle)
            if res == 0:
                return middle
            if res > 0:
                left = middle + 1
            else:
                right = middle - 1
        return left
