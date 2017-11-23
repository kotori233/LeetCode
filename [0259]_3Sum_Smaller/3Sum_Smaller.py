class Solution(object):

    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = 0
        nums.sort()
        n = len(nums)
        for i in range(n):
            left, right = i + 1, n - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] < target:
                    res += (right - left)
                    left += 1
                else:
                    right -= 1
        return res
