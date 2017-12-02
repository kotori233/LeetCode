class Solution(object):

    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        s = sorted(nums)
        for i in range(1, n, 2):
            nums[i] = s.pop()
        for i in range(0, n, 2):
            nums[i] = s.pop()
