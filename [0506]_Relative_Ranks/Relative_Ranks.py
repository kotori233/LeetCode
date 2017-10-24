class Solution(object):

    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = nums[:]
        nums.sort(reverse=True)
        sheet = {}
        j = 1
        for i in nums:
            sheet[i] = str(j)
            j += 1
        try:
            sheet[nums[0]] = 'Gold Medal'
            sheet[nums[1]] = 'Silver Medal'
            sheet[nums[2]] = 'Bronze Medal'
        except IndexError:
            pass
        j = 0
        for i in res:
            res[j] = sheet[i]
            j += 1
        return res
