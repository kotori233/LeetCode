from collections import defaultdict


class Solution(object):

    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        n = len(wall)
        sheet = defaultdict(int)
        sheet[0] = 0
        for i in range(n):
            for j in range(len(wall[i]) - 1):
                if j:
                    wall[i][j] += wall[i][j - 1]
                sheet[wall[i][j]] += 1
        return n - max(sheet.values())
