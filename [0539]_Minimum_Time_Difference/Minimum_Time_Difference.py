class Solution(object):

    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        timePoints = [60 * int(t[:2]) + int(t[-2:]) for t in timePoints]
        timePoints.sort()
        res = float('inf')
        for i in range(1, len(timePoints)):
            res = min(res, timePoints[i] - timePoints[i - 1])
        return min(res, timePoints[0] + 1440 - timePoints[-1])
