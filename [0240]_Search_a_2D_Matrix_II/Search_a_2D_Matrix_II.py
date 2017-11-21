class Solution(object):

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n = len(matrix)
        if n == 0:
            return False
        m = len(matrix[0])
        if m == 0:
            return False
        i, j = n - 1, 0
        while i >= 0 and j < m:
            if target == matrix[i][j]:
                return True
            if target > matrix[i][j]:
                j += 1
            else:
                i -= 1
        return False
