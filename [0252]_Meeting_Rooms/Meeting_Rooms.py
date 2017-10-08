class Solution(object):

    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List]
        :rtype: bool
        """
        if len(intervals) == 1:
            return True
        intervals.sort(key=lambda x: x[0])
        max_end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < max_end:
                return False
            if intervals[i][1] > max_end:
                max_end = intervals[i][1]
        return True
