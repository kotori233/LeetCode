class Solution(object):

    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        val = sum(nums)
        if val & 1 == 1:
            return False
        val >>= 1
        dp = [False for i in range(val + 1)]
        dp[0] = True
        for i in nums:
            for j in range(val, i - 1, -1):
                dp[j] = dp[j] | dp[j - i]
        return dp[val]
