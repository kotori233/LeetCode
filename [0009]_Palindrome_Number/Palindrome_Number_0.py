class Solution(object):

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x % 10 == 0 and x != 0:
            return True
        reversed_number = 0
        while reversed_number < x:
            reversed_number = reversed_number * 10 + x % 10
            x //= 10
        if x == reversed_number or x == reversed_number // 10:
            return True
        return False
