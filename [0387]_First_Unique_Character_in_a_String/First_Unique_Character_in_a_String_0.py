class Solution(object):

    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        sheet = {}
        for i in s:
            if i in sheet:
                sheet[i] += 1
            else:
                sheet[i] = 1
        for i in range(len(s)):
            if sheet[s[i]] == 1:
                return i
        return -1
