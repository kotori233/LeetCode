# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        target = sum - root.val
        if target == 0 and root.left is None and root.right is None:
            return True
        if root.left is not None:
            if self.hasPathSum(root.left, target):
                return True
        if root.right is not None:
            if self.hasPathSum(root.right, target):
                return True
        return False
