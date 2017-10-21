class Solution(object):

    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        m = min(nums)
        for i in nums:
            res += (i - m)
        return res
