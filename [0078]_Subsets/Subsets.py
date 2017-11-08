class Solution(object):

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        subres = []
        n = len(nums)
        start = 0
        while 1:
            for i in range(start, n):
                subres.append(nums[i])
                res.append(subres[:])
            try:
                subres.pop()
                start = nums.index(subres.pop()) + 1
            except IndexError:
                break
        return res
