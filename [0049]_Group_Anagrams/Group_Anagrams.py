class Solution(object):

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sheet = {}
        res = []
        for i in strs:
            m = ''.join(sorted(list(i)))
            if m in sheet:
                sheet[m].append(i)
            else:
                sheet[m] = [i]
        for i in sheet:
            res.append(sheet[i])
        return res
