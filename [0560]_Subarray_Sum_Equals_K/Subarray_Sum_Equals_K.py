from collections import defaultdict


class Solution(object):

    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sheet = defaultdict(int)
        sheet[0] = 1
        res = 0
        for i in range(len(nums)):
            if i:
                nums[i] += nums[i - 1]
            res += sheet[nums[i] - k]
            sheet[nums[i]] += 1
        return res
