class Solution(object):

    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            middle = (left + right) // 2
            if nums[middle] == nums[middle - 1]:
                if middle & 1:
                    left = middle + 1
                else:
                    right = middle - 2
            elif nums[middle] == nums[middle + 1]:
                if middle & 1:
                    right = middle - 1
                else:
                    left = middle + 2
            else:
                return nums[middle]
        return nums[left]
