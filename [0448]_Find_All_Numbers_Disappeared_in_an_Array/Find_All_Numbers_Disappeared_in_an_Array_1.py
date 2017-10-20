class Solution(object):

    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = []
        for i in range(n):
            temp = abs(nums[i]) - 1
            if nums[temp] > 0:
                nums[temp] *= -1
        for i in range(n):
            if nums[i] > 0:
                res.append(i + 1)
        return res
