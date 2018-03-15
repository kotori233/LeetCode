# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return
        i = nums.index(max(nums))
        root = TreeNode(nums[i])
        root.left = self.constructMaximumBinaryTree(nums[:i])
        root.right = self.constructMaximumBinaryTree(nums[i + 1:])
        return root
