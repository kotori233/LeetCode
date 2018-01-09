class Solution(object):

    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(matrix)
        m = len(matrix[0])
        res = [[10000 for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                if matrix[i][j]:
                    res[i][j] = min(res[i][j], res[i - 1]
                                    [j] + 1, res[i][j - 1] + 1)
                else:
                    res[i][j] = 0
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if matrix[i][j]:
                    if i < n - 1:
                        res[i][j] = min(res[i + 1][j] + 1, res[i][j])
                    if j < m - 1:
                        res[i][j] = min(res[i][j + 1] + 1, res[i][j])
        return res
