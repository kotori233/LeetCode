class Solution(object):

    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sheet, total, res = {0: -1}, 0, 0
        for i in range(len(nums)):
            total += (nums[i] << 1) - 1
            if total in sheet:
                res = max(res, i - sheet[total])
            else:
                sheet[total] = i
        return res
