class Solution(object):

    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        n = len(nums)
        nums = [a * i * i + b * i + c for i in nums]
        res = [0 for i in range(n)]
        left, right = 0, n - 1
        i = -1 if a > 0 else 0
        while left <= right:
            if a > 0:
                if nums[left] > nums[right]:
                    res[i] = nums[left]
                    left += 1
                else:
                    res[i] = nums[right]
                    right -= 1
                i -= 1
            else:
                if nums[left] < nums[right]:
                    res[i] = nums[left]
                    left += 1
                else:
                    res[i] = nums[right]
                    right -= 1
                i += 1
        return res
