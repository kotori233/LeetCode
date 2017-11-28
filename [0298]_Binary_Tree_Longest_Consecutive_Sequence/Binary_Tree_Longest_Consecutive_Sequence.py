# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0

        def preorder(root, preval, count):
            if root.val == preval + 1:
                count += 1
            else:
                self.res = max(self.res, count)
                count = 1
            if root.left is not None:
                preorder(root.left, root.val, count)
            if root.right is not None:
                preorder(root.right, root.val, count)

        if root is not None:
            preorder(root, root.val, 0)
        return self.res
