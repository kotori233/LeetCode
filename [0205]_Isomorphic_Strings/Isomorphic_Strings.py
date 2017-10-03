class Solution(object):

    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n = len(s)
        if n != len(t):
            return False
        if n < 2:
            return True
        sheet = {}
        for i in range(n):
            if s[i] in sheet:
                if sheet[s[i]] != t[i]:
                    return False
            else:
                if t[i] in sheet.values():
                    return False
                sheet[s[i]] = t[i]
        return True
