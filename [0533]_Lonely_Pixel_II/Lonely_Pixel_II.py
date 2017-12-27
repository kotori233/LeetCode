from collections import defaultdict


class Solution(object):

    def findBlackPixel(self, picture, N):
        """
        :type picture: List[List[str]]
        :type N: int
        :rtype: int
        """
        res = 0
        n = len(picture)
        if n == 0:
            return res
        m = len(picture[0])
        if m == 0:
            return res
        sheet = defaultdict(int)
        colCount = [0 for j in range(m)]
        for i in range(n):
            rowCount = 0
            for j in range(m):
                if picture[i][j] == 'B':
                    colCount[j] += 1
                    rowCount += 1
            if rowCount == N:
                sheet[''.join(picture[i])] += 1
        for each in sheet:
            if sheet[each] != N:
                continue
            for j in range(m):
                if each[j] == 'B' and colCount[j] == N:
                    res += N
        return res
