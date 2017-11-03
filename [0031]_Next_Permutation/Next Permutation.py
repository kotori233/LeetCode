class Solution(object):

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if not n:
            return
        i = n - 1
        while i:
            if nums[i] > nums[i - 1]:
                cur = i - 1
                break
            i -= 1
        if not i:
            nums.reverse()
            return
        i = n - 1
        while 1:
            if nums[i] > nums[cur]:
                nums[i], nums[cur] = nums[cur], nums[i]
                break
            i -= 1
        left, right = cur + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
