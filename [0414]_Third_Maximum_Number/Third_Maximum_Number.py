class Solution(object):

    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = second = third = None
        for i in nums:
            if i in (first, second, third):
                pass
            elif first is None or i > first:
                first, second, third = i, first, second
            elif second is None or i > second:
                second, third = i, second
            elif first is None or i > third:
                third = i
        if third is None:
            return first
        return third
