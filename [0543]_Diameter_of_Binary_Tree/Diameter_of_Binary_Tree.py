# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxpath = 0

        def lrd(root):
            if root.left is not None:
                lrd(root.left)
            if root.right is not None:
                lrd(root.right)
            update(root)

        def update(root):
            if root.left is None:
                left = -1
                root.left = TreeNode(-1)
            else:
                left = root.left.val
            if root.right is None:
                right = -1
                root.right = TreeNode(-1)
            else:
                right = root.right.val
            root.val = max(left, right) + 1
            self.maxpath = max(
                self.maxpath, root.left.val + root.right.val + 2)

        if root is None:
            return 0
        lrd(root)
        return self.maxpath
