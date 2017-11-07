class Solution(object):

    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        flag1 = False
        flag2 = False
        if 0 in matrix[0]:
            flag1 = True
        for i in range(m):
            if matrix[i][0] == 0:
                flag2 = True
                break
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if flag1:
            matrix[0] = [0] * n
        if flag2:
            for i in range(m):
                matrix[i][0] = 0
