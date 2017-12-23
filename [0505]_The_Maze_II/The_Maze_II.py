class Solution(object):

    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        def dfs(i, j):
            if i == destination[0] and j == destination[1]:
                return
            for d in dirs:
                x, y = i, j
                dis = distance[(i, j)]
                while 0 <= x < n and 0 <= y < m and maze[x][y] != 1:
                    x += d[0]
                    y += d[1]
                    dis += 1
                x -= d[0]
                y -= d[1]
                dis -= 1
                if (x, y) not in distance or dis < distance[(x, y)]:
                    distance[(x, y)] = dis
                    dfs(x, y)

        n = len(maze)
        m = len(maze[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        distance = {}
        distance[(start[0], start[1])] = 0
        dfs(start[0], start[1])
        return distance.get((destination[0], destination[1]), -1)
