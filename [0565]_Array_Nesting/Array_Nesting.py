class Solution(object):

    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def dfs(idx):
            count = 0
            while nums[idx] + 1:
                count += 1
                temp = nums[idx]
                nums[idx] = -1
                idx = temp
            return count

        res = 0
        for i in range(len(nums)):
            if nums[i] + 1:
                res = max(res, dfs(i))
        return res
