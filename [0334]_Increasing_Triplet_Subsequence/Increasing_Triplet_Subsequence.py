class Solution(object):

    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        pre1, pre2 = float('inf'), float('inf')
        for i in nums:
            if i > pre2:
                return True
            if i < pre1:
                pre1 = i
            elif pre1 < i < pre2:
                pre2 = i
        return False
