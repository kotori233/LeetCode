# Definition for a binary tree node.
# class TreeNode(object):
#
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

        def preorder(root):
            inc, dec = 0, 0
            for node in (root.left, root.right):
                if not node:
                    continue
                cinc, cdec = preorder(node)
                if node.val == root.val + 1:
                    inc = max(inc, cinc)
                elif node.val == root.val - 1:
                    dec = max(dec, cdec)
            self.res = max(self.res, inc + dec + 1)
            return inc + 1, dec + 1

        if root:
            preorder(root)
        return self.res
