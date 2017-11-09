class Solution(object):

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        n = len(nums)
        if n == 0:
            return False
        left, right = 0, n - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return True
            if nums[middle] < nums[right]:
                if nums[middle] < target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
            elif nums[middle] > nums[right]:
                if nums[left] <= target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            else:
                right -= 1
        return False
