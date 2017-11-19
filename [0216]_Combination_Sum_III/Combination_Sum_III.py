class Solution(object):

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.res = []

        def dfs(subres, nums, target):
            if len(subres) == k:
                if target == 0:
                    self.res.append(subres)
                return
            for i in range(len(nums)):
                dfs(subres + [nums[i]], nums[i + 1:], target - nums[i])

        dfs([], list(range(1, 10)), n)
        return self.res
