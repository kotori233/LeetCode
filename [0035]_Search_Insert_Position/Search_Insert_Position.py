class Solution(object):

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        try:
            pos = nums.index(target)
            return pos
        except:
            pass
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        left = 0
        right = len(nums) - 1
        middle = (right - left) // 2
        while middle:
            if nums[middle + left] < target:
                left += middle
            else:
                right = middle + left
            middle = (right - left) // 2
        return left + 1
