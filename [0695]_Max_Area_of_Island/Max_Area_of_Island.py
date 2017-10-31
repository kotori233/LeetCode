class Solution(object):

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.h, self.w = len(grid), len(grid[0])

        def update(i, j):
            res = 1
            grid[i][j] = 0
            for (x, y) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if -1 < i + x < self.h and -1 < j + y < self.w:
                    if grid[i + x][j + y] == 1:
                        res += update(i + x, j + y)
            return res

        m = 0
        for i in range(self.h):
            for j in range(self.w):
                if grid[i][j] == 1:
                    m = max(m, update(i, j))
        return m
