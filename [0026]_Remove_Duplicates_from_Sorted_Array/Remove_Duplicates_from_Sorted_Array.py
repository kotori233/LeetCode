class Solution(object):

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        n = 1
        for each in nums:
            if nums[n - 1] != each:
                n += 1
                nums[n - 1] = each
        return n
