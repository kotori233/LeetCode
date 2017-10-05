class Solution(object):

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        sheet = {}
        for i in s:
            if i in sheet:
                sheet[i] += 1
            else:
                sheet[i] = 1
        for i in t:
            if i not in sheet:
                return False
            else:
                sheet[i] -= 1
                if sheet[i] < 0:
                    return False
        return True
