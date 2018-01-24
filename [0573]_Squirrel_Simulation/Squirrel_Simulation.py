class Solution(object):

    def minDistance(self, height, width, tree, squirrel, nuts):
        """
        :type height: int
        :type width: int
        :type tree: List[int]
        :type squirrel: List[int]
        :type nuts: List[List[int]]
        :rtype: int
        """
        def d(x, y):
            return abs(x[0] - y[0]) + abs(x[1] - y[1])

        return 2 * sum(d(tree, nut) for nut in nuts) + \
            min(d(squirrel, nut) - d(tree, nut) for nut in nuts)
