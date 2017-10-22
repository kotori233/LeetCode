class Solution(object):

    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        if n == 1:
            return False
        for i in range(n // 2):
            if n % (i + 1) == 0 and s[:i + 1] * (n // (i + 1)) == s:
                return True
        return False
