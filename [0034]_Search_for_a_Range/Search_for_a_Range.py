class Solution(object):

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = [-1, -1]
        n = len(nums)
        if n == 0:
            return res
        left, right = 0, n - 1
        while left + 1 < right:
            middle = (left + right) // 2
            if nums[middle] > target:
                right = middle
            else:
                left = middle
        if nums[right] == target:
            res[1] = right
        elif nums[left] == target:
            res[1] = left
        left, right = 0, n - 1
        while left + 1 < right:
            middle = (left + right) // 2
            if nums[middle] < target:
                left = middle
            else:
                right = middle
        if nums[left] == target:
            res[0] = left
        elif nums[right] == target:
            res[0] = right
        return res
