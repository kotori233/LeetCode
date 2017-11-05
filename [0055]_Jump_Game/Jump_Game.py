class Solution(object):

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n == 1:
            return True
        m = nums[0]
        for i in range(1, n):
            if m < i:
                return False
            m = max(i + nums[i], m)
            if m > n - 2:
                return True
