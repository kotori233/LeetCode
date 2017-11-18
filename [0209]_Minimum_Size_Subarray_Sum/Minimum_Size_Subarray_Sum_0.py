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
        m = n + 1
        sums = [0 for i in range(n)]
        sums[0] = nums[0]
        for i in range(1, n):
            sums[i] = sums[i - 1] + nums[i]
        for i in range(n):
            left, right = i, n - 1
            while left <= right:
                middle = (left + right) // 2
                if sums[middle] - sums[i] + nums[i] >= s:
                    m = min(m, middle - i + 1)
                    right = middle - 1
                else:
                    left = middle + 1
        if m == n + 1:
            return 0
        return m
