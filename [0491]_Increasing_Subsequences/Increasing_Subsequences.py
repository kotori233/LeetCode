class Solution(object):

    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []

        def dfs(left, subres):
            if len(subres) > 1:
                self.res.append(subres[:])
            used = set()
            for i in range(left, n):
                if (subres and subres[-1] > nums[i]) or nums[i] in used:
                    continue
                used.add(nums[i])
                dfs(i + 1, subres + [nums[i]])

        n = len(nums)
        dfs(0, [])
        return self.res
