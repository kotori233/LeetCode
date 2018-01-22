class Solution(object):

    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = list(str(n))
        n = len(nums)
        for i in range(n - 1, -1, -1):
            if nums[i - 1] < nums[i]:
                break
        if i == 0:
            return -1
        for j in range(n - 1, i - 1, -1):
            if nums[j] > nums[i - 1]:
                nums[j], nums[i - 1] = nums[i - 1], nums[j]
                break
        res = int(''.join(nums[:i] + sorted(nums[i:])))
        if res > 0x7FFFFFFF:
            return -1
        return res
