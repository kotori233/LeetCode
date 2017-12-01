class Solution(object):

    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        res = 0
        sheet = {}
        for each in words:
            mask = 0
            for i in each:
                mask |= (1 << (ord(i) - 97))
            sheet[mask] = max(sheet.get(mask, 0), len(each))
            for j in sheet:
                if j & mask == 0:
                    res = max(res, sheet[j] * sheet[mask])
        return res
