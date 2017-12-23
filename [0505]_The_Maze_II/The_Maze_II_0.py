class Solution(object):

    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        n = len(maze)
        m = len(maze[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        distance = {}
        distance[(start[0], start[1])] = 0
        queue = [(start[0], start[1])]
        while queue:
            i, j = queue.pop(0)
            if i == destination[0] and j == destination[1]:
                return distance[(destination[0], destination[1])]
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
                    queue.append((x, y))
        return -1
