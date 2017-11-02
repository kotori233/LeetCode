class Solution(object):

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res, n = [], len(nums)
        if n < 3:
            return res
        nums.sort()
        for i in range(n - 2):
            if nums[i] > 0:
                break
            if i and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                temp = nums[left] + nums[right] + nums[i]
                if temp == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif temp < 0:
                    left += 1
                else:
                    right -= 1
        return res
