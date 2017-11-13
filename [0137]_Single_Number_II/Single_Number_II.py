class Solution(object):

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i = 0
        while 1:
            try:
                if nums[i] != nums[i + 1]:
                    return nums[i]
            except IndexError:
                return nums[-1]
            i += 3
