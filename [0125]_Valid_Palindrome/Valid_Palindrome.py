class Solution(object):

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length = len(s)
        if length == 0:
            return True
        i, j = 0, length - 1
        while j >= i:
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
