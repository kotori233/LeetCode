class Solution(object):

    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        res = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                target = nums[i] + nums[j]
                # 寻找不可能点
                left, right = j + 1, n
                while left < right:
                    middle = (left + right) // 2
                    if nums[middle] < target:
                        left = middle + 1
                    else:
                        right = middle
                res += (right - 1 - j)
        return res
