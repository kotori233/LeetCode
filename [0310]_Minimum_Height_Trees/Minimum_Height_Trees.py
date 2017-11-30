class Solution(object):

    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        sheet = {}
        for each in edges:
            sheet[each[0]] = sheet.get(each[0], []) + [each[1]]
            sheet[each[1]] = sheet.get(each[1], []) + [each[0]]
        skin = []
        for i in range(n):
            if len(sheet.get(i, [])) < 2:
                skin.append(i)
        while n > 2:
            n -= len(skin)
            new = []
            for i in skin:
                for j in sheet[i]:
                    sheet[j].remove(i)
                    if len(sheet[j]) == 1:
                        new.append(j)
            skin = new
        return skin
