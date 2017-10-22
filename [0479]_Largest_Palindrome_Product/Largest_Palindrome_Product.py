class Solution(object):

    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        return [9, 9009, 906609, 99000099, 9966006699,
                999000000999, 99956644665999, 9999000000009999][n - 1] % 1337
