class Solution(object):

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res, n = [], len(nums)
        if n < 3:
            return res
        nums.sort()
        min_sum = nums[0] + nums[1] + nums[2]
        if min_sum >= target:
            return min_sum
        max_sum = nums[-1] + nums[-2] + nums[-3]
        if max_sum <= target:
            return max_sum
        for i in range(len(nums)):
            if i and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                temp = nums[i] + nums[left] + nums[right]
                if temp == target:
                    return target
                if temp < target:
                    min_sum = max(min_sum, temp)
                    left += 1
                else:
                    max_sum = min(max_sum, temp)
                    right -= 1
        if max_sum - target > target - min_sum:
            return min_sum
        return max_sum
