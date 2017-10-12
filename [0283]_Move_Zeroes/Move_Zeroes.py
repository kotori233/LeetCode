class Solution(object):

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if 0 not in nums:
            return
        count = 0
        while 0 in nums:
            nums.remove(0)
            count += 1
        nums += [0] * count
