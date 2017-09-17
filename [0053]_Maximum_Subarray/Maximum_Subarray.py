class Solution(object):

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        g = nums[0]
        l = 0
        for i in range(len(nums)):
            if l < 0:
                l = 0
            l += nums[i]
            g = max(l, g)
        return g
