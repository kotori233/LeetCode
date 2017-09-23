# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def deep(tree):
            if tree is None:
                return 0
            return max(deep(tree.left), deep(tree.right)) + 1

        if root is None:
            return True
        if abs(deep(root.left) - deep(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
