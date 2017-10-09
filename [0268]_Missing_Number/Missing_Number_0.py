class Solution(object):

    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res, j = len(nums), 0
        for i in nums:
            res ^= (i ^ j)
            j += 1
        return res
