class Solution(object):

    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = []
        for i in range(n):
            while nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]:
                temp = nums[i] - 1
                nums[i], nums[temp] = nums[temp], nums[i]
        for i in range(n):
            if nums[i] != i + 1:
                res.append(i + 1)
        return res
