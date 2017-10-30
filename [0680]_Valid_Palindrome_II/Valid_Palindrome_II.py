class Solution(object):

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isPalindrome(s, flag):
            left, right = 0, len(s) - 1
            while left < right:
                if s[left] != s[right]:
                    if flag:
                        return False
                    self.flag = True
                    return isPalindrome(s[left + 1: right + 1], True) or \
                        isPalindrome(s[left: right], True)
                left += 1
                right -= 1
            return True

        if len(s) < 3:
            return True
        return isPalindrome(s, False)
