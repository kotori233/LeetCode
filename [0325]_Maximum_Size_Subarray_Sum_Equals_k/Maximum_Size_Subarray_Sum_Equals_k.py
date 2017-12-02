class Solution(object):

    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sheet = {0: 0}
        sums, res = 0, 0
        for i in range(1, len(nums) + 1):
            sums += nums[i - 1]
            target = sums - k
            if target in sheet:
                res = max(res, i - sheet[target])
            if sums not in sheet:
                sheet[sums] = i
        return res
