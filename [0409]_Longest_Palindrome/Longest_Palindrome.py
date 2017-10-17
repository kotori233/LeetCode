class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        sheet = {}
        count = res = 0
        for i in s:
            if i in sheet:
                sheet[i] += 1
            else:
                sheet[i] = 1
        for i in sheet.values():
            if i % 2 != 0:
                count += 1
            res += i
        if count == 0:
            return res
        return res - count + 1
