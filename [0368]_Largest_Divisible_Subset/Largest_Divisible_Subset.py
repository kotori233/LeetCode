class Solution(object):

    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = []
        if n == 0:
            return res
        dp = [1 for i in range(n)]
        pre = [None for i in range(n)]
        nums.sort()
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    pre[i] = j
        idx = dp.index(max(dp))
        while idx is not None:
            res.insert(0, nums[idx])
            idx = pre[idx]
        return res
