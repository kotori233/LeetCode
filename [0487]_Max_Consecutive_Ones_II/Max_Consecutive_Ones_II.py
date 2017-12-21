class Solution(object):

    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if 0 not in nums:
            return len(nums)
        res, pre, cur = 0, 0, 0
        for i in nums:
            if i == 1:
                cur += 1
            else:
                pre, cur = cur, 0
            res = max(res, pre + cur + 1)
        return res
