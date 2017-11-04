class Solution(object):

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []

        def create(nums, subres, own):
            if len(subres) == n:
                self.res.append(subres[:])
            pre = None
            for i in range(n):
                if nums[i] == pre:
                    continue
                if i not in own:
                    subres.append(nums[i])
                    own.append(i)
                    pre = nums[i]
                    create(nums, subres, own)
                    subres.pop()
                    own.pop()

        nums.sort()
        n = len(nums)
        create(nums, [], [])
        return self.res
