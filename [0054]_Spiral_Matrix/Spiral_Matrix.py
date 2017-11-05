class Solution(object):

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if matrix == []:
            return res
        n, m = len(matrix[0]), len(matrix)
        k = 0
        while k < n - k - 1 and k < m - k - 1:
            for j in range(k, n - k - 1):
                res.append(matrix[k][j])
            for i in range(k, m - k - 1):
                res.append(matrix[i][n - k - 1])
            for j in range(n - k - 1, k, -1):
                res.append(matrix[m - k - 1][j])
            for i in range(m - k - 1, k, -1):
                res.append(matrix[i][k])
            k += 1
        if m <= n and m % 2 == 1:
            for j in range(k, n - k):
                res.append(matrix[m // 2][j])
        if n < m and n % 2 == 1:
            for i in range(k, m - k):
                res.append(matrix[i][n // 2])
        return res
