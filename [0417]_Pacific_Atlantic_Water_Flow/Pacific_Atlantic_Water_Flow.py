class Solution(object):

    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        def dfs(i, j, sheet, pre):
            if i < 0 or j < 0 or i > n - 1 or j > m - 1 or sheet[i][j]:
                return
            if matrix[i][j] < pre:
                return
            sheet[i][j] = True
            pre = matrix[i][j]
            dfs(i - 1, j, sheet, pre)
            dfs(i, j - 1, sheet, pre)
            dfs(i + 1, j, sheet, pre)
            dfs(i, j + 1, sheet, pre)

        res = []
        n = len(matrix)
        if n == 0:
            return res
        m = len(matrix[0])
        if m == 0:
            return res
        pacific = [[False for j in range(m)] for i in range(n)]
        atlantic = [[False for j in range(m)] for i in range(n)]
        for i in range(n):
            dfs(i, 0, pacific, float('-inf'))
            dfs(i, m - 1, atlantic, float('-inf'))
        for j in range(m):
            dfs(0, j, pacific, float('-inf'))
            dfs(n - 1, j, atlantic, float('-inf'))
        for i in range(n):
            for j in range(m):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i, j])
        return res
