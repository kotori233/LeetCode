class Solution(object):

    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        m1 = nums[0] * nums[1] * nums[-1]
        m2 = nums[-1] * nums[-2] * nums[-3]
        return max(m1, m2)
