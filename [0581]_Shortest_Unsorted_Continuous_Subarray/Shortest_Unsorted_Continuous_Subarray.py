class Solution(object):

    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        old = nums[:]
        nums.sort()
        new = nums
        i = 0
        try:
            while 1:
                if old[i] != new[i]:
                    left = i
                    break
                i += 1
        except IndexError:
            return 0
        i = len(nums) - 1
        while 1:
            if old[i] != new[i]:
                right = i
                break
            i -= 1
        return right - left + 1
