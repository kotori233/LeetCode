class Solution(object):

    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        res = 0
        n = len(picture)
        if n == 0:
            return res
        m = len(picture[0])
        if m == 0:
            return res
        rows, cols = [0 for i in range(n)], [0 for j in range(m)]
        whichcol = [0 for i in range(n)]
        for i in range(n):
            for j in range(m):
                if picture[i][j] == 'B':
                    rows[i] += 1
                    cols[j] += 1
                    whichcol[i] = j
        for i in range(n):
            if rows[i] == 1 and cols[whichcol[i]] == 1:
                res += 1
        return res
