class Solution(object):

    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List]
        :rtype: int
        """
        start, end = [], []
        n = len(intervals)
        for i in intervals:
            start.append(i[0])
            end.append(i[1])
        start.sort()
        end.sort()
        j, res = 0, 0
        for i in range(n):
            if start[i] < end[j]:
                res += 1
            else:
                j += 1
        return res
