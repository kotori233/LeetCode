class Solution(object):

    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        side = 0
        n = len(matrix)
        if n == 0:
            return 0
        m = len(matrix[0])
        if m == 0:
            return 0
        if '1' in matrix[0]:
            side = 1
        if side == 0:
            for i in range(n):
                if matrix[i][0] == '1':
                    side = 1
                    break
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == '1':
                    matrix[i][j] = min(int(matrix[i - 1][j]),
                                       int(matrix[i][j - 1]),
                                       int(matrix[i - 1][j - 1])) + 1
                    side = max(side, matrix[i][j])
        return side * side
