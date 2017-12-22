class Solution(object):

    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        n = len(matrix)
        if n == 0:
            return res
        m = len(matrix[0])
        if m == 0:
            return res
        i, j, k, dirs = 0, 0, 0, ((-1, 1), (1, -1))
        for x in range(m * n):
            res.append(matrix[i][j])
            i += dirs[k][0]
            j += dirs[k][1]
            if i > n - 1:
                i, k = n - 1, 1 - k
                j += 2
            if j > m - 1:
                j, k = m - 1, 1 - k
                i += 2
            if i < 0:
                i, k = 0, 1 - k
            if j < 0:
                j, k = 0, 1 - k
        return res
