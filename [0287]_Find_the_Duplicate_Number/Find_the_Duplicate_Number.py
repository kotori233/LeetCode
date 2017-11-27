class Solution(object):

    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 1, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            count = 0
            for i in nums:
                if i <= middle:
                    count += 1
            if count > middle:
                right = middle - 1
            else:
                left = middle + 1
        return left
