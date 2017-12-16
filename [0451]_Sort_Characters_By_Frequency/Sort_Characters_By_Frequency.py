class Solution(object):

    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        sheet = {}
        for i in s:
            sheet[i] = sheet.get(i, 0) + 1
        res = ''
        for key, val in sorted(sheet.items(), key=lambda x: -x[1]):
            res += (key * val)
        return res
