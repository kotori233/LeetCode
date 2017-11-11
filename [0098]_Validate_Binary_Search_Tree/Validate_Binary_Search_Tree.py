# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.temp = None

        def inorder(root):
            if root.left is not None:
                if not inorder(root.left):
                    return False
            if root.val <= self.temp:
                return False
            self.temp = root.val
            if root.right is not None:
                if not inorder(root.right):
                    return False
            return True

        if root is None:
            return True
        return inorder(root)
