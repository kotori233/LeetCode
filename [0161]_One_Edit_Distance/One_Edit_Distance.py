class Solution(object):

    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) < len(t):
            s, t = t, s
        n1 = len(s)
        n2 = len(t)
        if n1 - n2 > 1:
            return False
        if n1 == n2:
            count = 0
            for i in range(n1):
                if s[i] != t[i]:
                    count += 1
                    if count > 1:
                        return False
            return count != 0
        else:
            for i in range(n2):
                if s[i] != t[i]:
                    if s[i + 1:] != t[i:]:
                        return False
            return True
