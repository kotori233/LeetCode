class Solution(object):

    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n1, n2 = len(s), len(t)
        i, j = 0, 0
        while i < n1 and j < n2:
            if s[i] == t[j]:
                i += 1
            j += 1
        if i == n1:
            return True
        return False
