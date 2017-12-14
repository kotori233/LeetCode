# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

import bisect


class Solution(object):

    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        ret = sorted([(x.start, i) for i, x in enumerate(intervals)])
        res = []
        n = len(intervals)
        for each in intervals:
            # -1辅助使排在同each.end值的第一个
            idx = bisect.bisect_right(ret, (each.end, -1))
            res.append(ret[idx][1] if idx < n else -1)
        return res
