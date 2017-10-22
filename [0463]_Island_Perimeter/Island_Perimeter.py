class Solution(object):

    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        wide = len(grid)
        height = len(grid[0])
        count, bonder = 0, 0
        for i in range(wide):
            for j in range(height):
                count += grid[i][j]
                if i and grid[i][j] == 1 and grid[i - 1][j] == 1:
                    bonder += 1
                if j and grid[i][j] == 1 and grid[i][j - 1] == 1:
                    bonder += 1
        return count * 4 - bonder * 2
