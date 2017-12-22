class Solution(object):

    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack, n = [], len(nums)
        res = [-1 for i in range(n)]
        for i in range(2 * n):
            t = i % n
            while stack and nums[stack[-1]] < nums[t]:
                res[stack.pop()] = nums[t]
            if i < n:
                stack.append(i)
        return res
