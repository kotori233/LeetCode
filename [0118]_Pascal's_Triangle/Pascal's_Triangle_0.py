class Solution(object):

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        def triangles():
            L = [1]
            n = 0
            yield L
            while 1:
                next_L = [1]
                for i in range(n):
                    next_L.append(L[i] + L[i + 1])
                next_L.append(1)
                L = next_L[:]
                n = n + 1
                yield next_L

        if numRows == 0:
            return []
        n = 0
        tri = []
        for t in triangles():
            tri.append(t)
            n = n + 1
            if n == numRows:
                break
        return tri
