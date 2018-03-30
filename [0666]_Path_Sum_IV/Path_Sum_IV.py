class Solution(object):

    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sheet = {1: 0}
        leaves = {1}
        for each in nums:
            pos, val = each // 10, each % 10
            level, x = pos // 10, pos % 10
            parent = (level - 1) * 10 + (x + 1) // 2
            sheet[pos] = sheet[parent] + val
            leaves.add(pos)
            if parent in leaves:
                leaves.remove(parent)
        return sum(sheet[pos] for pos in leaves)
