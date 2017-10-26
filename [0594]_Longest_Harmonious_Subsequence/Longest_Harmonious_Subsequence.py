class Solution(object):

    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sheet = {}
        for i in nums:
            sheet[i] = sheet.get(i, 0) + 1
        max_len = 0
        for i in sheet:
            try:
                length = sheet[i] + sheet[i + 1]
                max_len = max(max_len, length)
            except KeyError:
                pass
        return max_len
