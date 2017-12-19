class Solution(object):

    def isConvex(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        def crossProduct(p0, p1, p2):
            x0, y0 = p0
            x1, y1 = p1
            x2, y2 = p2
            return (x1 - x0) * (y2 - y1) - (x2 - x1) * (y1 - y0)

        n = len(points)
        last = 0
        for i in range(n):
            p0, p1, p2 = points[i], points[(i + 1) % n], points[(i + 2) % n]
            p = crossProduct(p0, p1, p2)
            if p * last < 0:
                return False
            last = p
        return True
