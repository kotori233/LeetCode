class Solution(object):

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp = 0
        for i in nums:
            temp ^= i
        flag = temp & (~(temp - 1))
        res = [0, 0]
        for i in nums:
            if i & flag == 0:
                res[0] ^= i
            else:
                res[1] ^= i
        return res
