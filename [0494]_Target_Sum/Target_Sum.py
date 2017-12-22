class Solution(object):

    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        sum_nums = sum(nums)
        if sum_nums < S or (sum_nums + S) % 2:
            return 0
        target = (sum_nums + S) // 2
        dp = [0 for i in range(target + 1)]
        dp[0] = 1
        for i in nums:
            for j in range(target, i - 1, -1):
                dp[j] += dp[j - i]
        return dp[target]
