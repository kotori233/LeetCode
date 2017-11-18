class Solution(object):

    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        n = len(nums)
        left, right = 0, 0
        temp, m = 0, n + 1
        while right < n:
            while temp < s and right < n:
                temp += nums[right]
                right += 1
            while temp >= s:
                m = min(right - left, m)
                temp -= nums[left]
                left += 1
        if m == n + 1:
            return 0
        return m
