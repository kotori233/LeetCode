class Solution(object):

    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        end = float('-inf')
        for each in sorted(points):
            if each[0] > end:
                res += 1
                end = each[1]
            else:
                end = min(end, each[1])
        return res
