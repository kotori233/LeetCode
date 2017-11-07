class Solution(object):

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        for i in range(m):
            for j in range(n):
                obstacleGrid[i][j] = 1 - obstacleGrid[i][j]
                if (i or j) and obstacleGrid[i][j] != 0:
                    obstacleGrid[i][j] = 0
                    if i:
                        obstacleGrid[i][j] += obstacleGrid[i - 1][j]
                    if j:
                        obstacleGrid[i][j] += obstacleGrid[i][j - 1]
        return obstacleGrid[m - 1][n - 1]
