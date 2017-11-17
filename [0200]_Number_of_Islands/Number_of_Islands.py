class Solution(object):

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.res = 0

        def dfs(i, j):
            grid[i][j] = '0'
            if i and grid[i - 1][j] == '1':
                dfs(i - 1, j)
            if j and grid[i][j - 1] == '1':
                dfs(i, j - 1)
            if i < n - 1 and grid[i + 1][j] == '1':
                dfs(i + 1, j)
            if j < m - 1 and grid[i][j + 1] == '1':
                dfs(i, j + 1)

        n = len(grid)
        if n == 0:
            return self.res
        m = len(grid[0])
        if m == 0:
            return self.res
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    dfs(i, j)
                    self.res += 1
        return self.res
