class Solution(object):

    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List]
        :rtype: int
        """
        sheet = {}
        res, rooms = 0, 0
        for i in intervals:
            sheet[i[0]] = 1
            sheet[i[1]] = -1
        for i in sorted(sheet.keys()):
            rooms += sheet[i]
            res = max(res, rooms)
        return res
