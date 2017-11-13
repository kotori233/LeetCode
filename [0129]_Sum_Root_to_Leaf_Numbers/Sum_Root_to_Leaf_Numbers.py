# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = []

        def dfs(root, subres):
            if root.left is None and root.right is None:
                self.res.append(subres * 10 + root.val)
                return
            if root.left is not None:
                dfs(root.left, subres * 10 + root.val)
            if root.right is not None:
                dfs(root.right, subres * 10 + root.val)

        if root is None:
            return 0
        dfs(root, 0)
        return sum(self.res)
