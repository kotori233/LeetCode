class Solution(object):

    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        res = 0
        for i in range(n - 1, 1, -1):
            left, right = 0, i - 1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    # 定right,i 变left
                    res += (right - left)
                    right -= 1
                else:
                    left += 1
        return res
