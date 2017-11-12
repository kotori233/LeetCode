# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        cur = root
        while cur:
            if cur.left is not None:
                temp = cur.right
                cur.right = cur.left
                cur.left = None
                pred = cur.right
                while pred.right:
                    pred = pred.right
                pred.right = temp
            cur = cur.right
