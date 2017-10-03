class Solution(object):

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return False
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False
