class Solution(object):

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == [] or matrix == [[]]:
            return False
        m = len(matrix)
        n = len(matrix[0])
        if target < matrix[0][0] or target > matrix[m - 1][n - 1]:
            return False
        level = 0
        for i in range(1, m):
            if target < matrix[i][0]:
                break
            level += 1
        if target > matrix[level][-1]:
            return False
        return target in matrix[level]
