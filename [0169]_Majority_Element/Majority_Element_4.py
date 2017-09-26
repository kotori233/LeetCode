class Solution(object):

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        major = count = 0
        for i in nums:
            if count == 0:
                major = i
                count = 1
            else:
                count += 1 if major == i else -1
        return major
