class Solution(object):

    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        if n == 0:
            return 0
        m = len(grid[0])
        if m == 0:
            return 0
        rowkill, res = 0, 0
        colkill = [0 for j in range(m)]
        for i in range(n):
            for j in range(m):
                if j == 0 or grid[i][j - 1] == 'W':
                    rowkill = 0
                    for k in range(j, m):
                        if grid[i][k] == 'W':
                            break
                        if grid[i][k] == 'E':
                            rowkill += 1
                if i == 0 or grid[i - 1][j] == 'W':
                    colkill[j] = 0
                    for k in range(i, n):
                        if grid[k][j] == 'W':
                            break
                        if grid[k][j] == 'E':
                            colkill[j] += 1
                if grid[i][j] == '0':
                    res = max(res, rowkill + colkill[j])
        return res
