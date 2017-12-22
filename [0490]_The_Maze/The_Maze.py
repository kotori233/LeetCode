class Solution(object):

    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        def dfs(i, j):
            if i == destination[0] and j == destination[1]:
                return True
            if (i, j) in cache:
                return cache[(i, j)]
            maze[i][j] = -1
            for d in dirs:
                x, y = i, j
                while 0 <= x < n and 0 <= y < m and maze[x][y] != 1:
                    x += d[0]
                    y += d[1]
                x -= d[0]
                y -= d[1]
                if maze[x][y] != -1 and dfs(x, y):
                    return True
            return False

        n = len(maze)
        m = len(maze[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        cache = {}
        return dfs(start[0], start[1])
