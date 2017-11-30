class Solution(object):

    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if (not A) or (not B):
            return []
        n, m, p = len(A), len(B[0]), len(B)
        res = [[0 for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(p):
                if A[i][j]:
                    for k in range(m):
                        if B[j][k]:
                            res[i][k] += A[i][j] * B[j][k]
        return res
