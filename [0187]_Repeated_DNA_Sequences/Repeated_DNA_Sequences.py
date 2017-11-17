class Solution(object):

    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = set()
        sheet = set()
        for i in range(len(s) - 9):
            temp = s[i:i + 10]
            if temp in sheet:
                res.add(temp)
            else:
                sheet.add(temp)
        return list(res)
