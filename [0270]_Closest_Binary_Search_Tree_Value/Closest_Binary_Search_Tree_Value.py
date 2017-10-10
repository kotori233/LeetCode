# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type value: int
        :rtype: int
        """
        res = root.val
        while root is not None:
            if abs(target - res) > abs(target - root.val):
                res = root.val
            if target > root.val:
                root = root.right
            else:
                root = root.left
        return res
