class Solution(object):

    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if not timeSeries:
            return 0
        res = 0
        for i in range(1, len(timeSeries)):
            diff = timeSeries[i] - timeSeries[i - 1]
            if diff > duration:
                res += duration
            else:
                res += diff
        return res + duration
