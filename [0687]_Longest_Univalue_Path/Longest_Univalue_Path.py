# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.deepest = 0

        def lrd(root):
            if root.left is not None:
                lrd(root.left)
            if root.right is not None:
                lrd(root.right)
            update(root)

        def update(root):
            if root.left is not None and root.left.val[0] == root.val:
                left = root.left.val[1] + 1
            else:
                left = 0
            if root.right is not None and root.right.val[0] == root.val:
                right = root.right.val[1] + 1
            else:
                right = 0
            root.val = [root.val, max(right, left)]
            self.deepest = max(self.deepest, left + right)

        if root is None:
            return 0
        lrd(root)
        return self.deepest
