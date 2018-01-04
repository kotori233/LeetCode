class Solution(object):

    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(matrix)
        m = len(matrix[0])
        queue = []
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    queue.append((i, j))
                else:
                    matrix[i][j] = float('inf')
        for i, j in queue:
            t = matrix[i][j] + 1
            for x, y in ((i, 1 + j), (i, j - 1), (i + 1, j), (i - 1, j)):
                if -1 < x < n and -1 < y < m and matrix[x][y] > matrix[i][j]:
                    matrix[x][y] = t
                    queue.append((x, y))
        return matrix
