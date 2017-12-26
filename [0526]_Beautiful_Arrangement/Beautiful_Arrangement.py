class Solution(object):

    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        self.cache = {}

        def dfs(idx, nums):
            if not nums:
                return 1
            key = idx, tuple(nums)
            if key in self.cache:
                return self.cache[key]
            res = 0
            for i, v in enumerate(nums):
                if not v % idx or not idx % v:
                    res += dfs(idx + 1, nums[:i] + nums[i + 1:])
            self.cache[key] = res
            return res

        return dfs(1, range(1, N + 1))
