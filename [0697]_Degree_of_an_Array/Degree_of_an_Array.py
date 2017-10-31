class Solution(object):

    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sheet = {}
        for i in range(len(nums)):
            each = nums[i]
            if each in sheet:
                sheet[each][0] += 1
                sheet[each][2] = i
            else:
                sheet[each] = [1, i, i]
        m = 0
        for i in sheet:
            if sheet[i][0] > m:
                m = sheet[i][0]
                res = sheet[i][2] - sheet[i][1] + 1
            if sheet[i][0] == m:
                res = min(res, sheet[i][2] - sheet[i][1] + 1)
        return res
