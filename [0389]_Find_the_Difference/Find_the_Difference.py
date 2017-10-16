class Solution(object):

    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        sheet = {}
        for i in s:
            if i in sheet:
                sheet[i] += 1
            else:
                sheet[i] = 1
        for i in t:
            if i not in sheet or sheet[i] == 0:
                return i
            sheet[i] -= 1
