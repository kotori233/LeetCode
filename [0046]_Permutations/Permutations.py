class Solution(object):

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []

        def create(nums, subres):
            if len(subres) == n:
                self.res.append(subres[:])
            for i in nums:
                if i in subres:
                    continue
                subres.append(i)
                create(nums, subres)
                subres.pop()

        n = len(nums)
        create(nums, [])
        return self.res
