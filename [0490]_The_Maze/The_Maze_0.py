class Solution(object):

    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        n = len(maze)
        m = len(maze[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = [(start[0], start[1])]
        visited = set()
        while queue:
            i, j = queue.pop(0)
            if i == destination[0] and j == destination[1]:
                return True
            visited.add((i, j))
            for d in dirs:
                x, y = i, j
                while 0 <= x < n and 0 <= y < m and maze[x][y] != 1:
                    x += d[0]
                    y += d[1]
                x -= d[0]
                y -= d[1]
                if (x, y) not in visited:
                    queue.append((x, y))
        return False
