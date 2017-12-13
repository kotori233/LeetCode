# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution(object):

    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        n = len(intervals)
        if n == 0:
            return 0
        intervals.sort(key=lambda x: (x.start, x.end))
        res, pre = 0, 0
        for i in range(1, n):
            if intervals[i].start < intervals[pre].end:
                if intervals[i].end < intervals[pre].end:
                    pre = i
                res += 1
            else:
                pre = i
        return res
