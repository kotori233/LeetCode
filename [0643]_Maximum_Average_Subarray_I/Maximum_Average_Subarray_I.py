class Solution(object):

    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        vals = pre = sum(nums[:k])
        for i in range(k, len(nums)):
            pre = pre - nums[i - k] + nums[i]
            vals = max(vals, pre)
        return 1.0 * vals / k
