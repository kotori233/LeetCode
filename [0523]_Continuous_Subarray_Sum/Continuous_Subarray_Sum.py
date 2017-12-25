class Solution(object):

    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        for i in range(n):
            total = nums[i]
            for j in range(i + 1, n):
                total += nums[j]
                if total == k:
                    return True
                if k and not total % k:
                    return True
        return False
