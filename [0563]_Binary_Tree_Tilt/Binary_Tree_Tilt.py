# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.tilt = 0

        def lrd(root):
            if root.left is not None:
                lrd(root.left)
            if root.right is not None:
                lrd(root.right)
            update(root)

        def update(root):
            if root.left is None:
                left = 0
            else:
                left = root.left.val
            if root.right is None:
                right = 0
            else:
                right = root.right.val
            root.val += left + right
            self.tilt += abs(left - right)

        if root is None:
            return 0
        lrd(root)
        return self.tilt
