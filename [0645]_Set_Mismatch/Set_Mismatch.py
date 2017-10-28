class Solution(object):

    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        r1 = sum(nums) - sum(set(nums))
        r2 = sum(range(len(nums) + 1)) - sum(nums) + r1
        return [r1, r2]
