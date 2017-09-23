# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums == []:
            return None
        middle = len(nums) // 2
        tree = TreeNode(nums[middle])
        left_nums = nums[:middle]
        right_nums = nums[middle + 1:]
        if left_nums != []:
            tree.left = self.sortedArrayToBST(left_nums)
        if right_nums != []:
            tree.right = self.sortedArrayToBST(right_nums)
        return tree
