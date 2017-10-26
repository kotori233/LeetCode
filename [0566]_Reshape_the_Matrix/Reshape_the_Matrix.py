class Solution(object):

    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        height = len(nums)
        width = len(nums[0])
        if height * width != r * c:
            return nums
        p, q = 0, 0
        res, child = [], []
        for i in range(height):
            for j in range(width):
                child.append(nums[i][j])
                q += 1
                if q == c:
                    res.append(child)
                    child = []
                    p += 1
                    q = 0
        return res
