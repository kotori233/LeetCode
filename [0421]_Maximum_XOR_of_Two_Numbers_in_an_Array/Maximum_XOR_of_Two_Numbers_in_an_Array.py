class Solution(object):

    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mask, res = 0, 0
        for i in range(32, -1, -1):
            mask |= (1 << i)
            prefix = {k & mask for k in nums}
            expect = res | (1 << i)
            for j in prefix:
                if j ^ expect in prefix:
                    res = expect
                    break
        return res
