class Solution(object):

    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = []
        for i in range(n):
            nums[nums[i] % (n + 1) - 1] += (n + 1)
        for i in range(n):
            if nums[i] // (n + 1) == 0:
                res.append(i + 1)
        return res
