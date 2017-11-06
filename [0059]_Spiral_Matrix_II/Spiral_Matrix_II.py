class Solution(object):

    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0 for i in range(n)] for i in range(n)]
        k, p = 0, 1
        while k < n - k - 1:
            for j in range(k, n - k - 1):
                res[k][j] = p
                p += 1
            for i in range(k, n - k - 1):
                res[i][n - k - 1] = p
                p += 1
            for j in range(n - k - 1, k, -1):
                res[n - k - 1][j] = p
                p += 1
            for i in range(n - k - 1, k, -1):
                res[i][k] = p
                p += 1
            k += 1
        if n % 2 == 1:
            res[n // 2][n // 2] = n * n
        return res
