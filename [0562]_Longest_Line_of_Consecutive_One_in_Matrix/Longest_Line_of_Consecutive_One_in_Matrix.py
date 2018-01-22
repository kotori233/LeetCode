class Solution(object):

    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        res = 0
        n = len(M)
        if n == 0:
            return res
        m = len(M[0])
        if m == 0:
            return res
        diag = [[0 for j in range(m)] for i in range(n)]
        for i in range(n):
            count = 0
            for j in range(m):
                count = (count + 1) * M[i][j]
                diag[i][j] = M[i][j]
                if i and j and M[i][j] and diag[i - 1][j - 1]:
                    diag[i][j] += diag[i - 1][j - 1]
                res = max(res, count, diag[i][j])
        print(diag)
        diag = [[0 for j in range(m)] for i in range(n)]
        for j in range(m):
            count = 0
            for i in range(n):
                count = (count + 1) * M[i][j]
                diag[i][j] = M[i][j]
                if i < n - 1 and j and M[i][j] and diag[i + 1][j - 1]:
                    diag[i][j] += diag[i + 1][j - 1]
                res = max(res, count, diag[i][j])
        print(diag)
        return res
