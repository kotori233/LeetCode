class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        n = len(matrix) + 1
        if n == 1:
            return
        m = len(matrix[0]) + 1
        if m == 1:
            return
        self.ret = [[0 for i in range(m)] for j in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                self.ret[i][j] = self.ret[i - 1][j] + self.ret[i][j - 1] + \
                    matrix[i - 1][j - 1] - self.ret[i - 1][j - 1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.ret[row2 + 1][col2 + 1] + self.ret[row1][col1] - \
            self.ret[row2 + 1][col1] - self.ret[row1][col2 + 1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
