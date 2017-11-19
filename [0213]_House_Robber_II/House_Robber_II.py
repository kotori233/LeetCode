class Solution(object):

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return sum(nums)
        ppre, pre = 0, nums[0]
        for i in range(2, n):
            ppre, pre = pre, max(pre, ppre + nums[i - 1])
        m = pre
        ppre, pre = 0, nums[1]
        for i in range(3, n + 1):
            ppre, pre = pre, max(pre, ppre + nums[i - 1])
        return max(m, pre)
