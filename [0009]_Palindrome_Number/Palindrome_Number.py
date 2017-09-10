class Solution(object):

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x < 10:
            return True
        n = 1
        while x // n >= 10:
            n *= 10
        while x:
            left = x // n
            right = x % 10
            if left != right:
                return False
            x = (x % n) // 10
            n //= 100
        return True
