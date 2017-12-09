class Solution(object):

    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = -1
        for x in s:
            i = t.find(x, i + 1)
            if i == -1:
                return False
        return True
