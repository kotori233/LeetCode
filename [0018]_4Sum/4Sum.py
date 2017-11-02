class Solution(object):

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res, n = [], len(nums)
        if n < 4:
            return res
        nums.sort()
        for i in range(n - 3):
            if i and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                t = target - nums[i] - nums[j]
                left, right = j + 1, n - 1
                while left < right:
                    temp = nums[left] + nums[right] - t
                    if temp == 0:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif temp > 0:
                        right -= 1
                    else:
                        left += 1
        return res
