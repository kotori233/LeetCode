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
        def path(root, val):
            if root is None or root.val != val:
                return 0
            return max(path(root.left, val), path(root.right, val)) + 1

        if root is None:
            return 0
        temp = path(root.left, root.val) + path(root.right, root.val)
        return max(temp, self.longestUnivaluePath(root.left),
                   self.longestUnivaluePath(root.right))
