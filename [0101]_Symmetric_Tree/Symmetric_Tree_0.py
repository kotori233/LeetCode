# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def each_same(p, q):
            if p is None and q is None:
                return True
            if p is not None and q is not None:
                if p.val == q.val:
                    key = each_same(p.left, q.right) and each_same(
                        p.right, q.left)
                    return key
            return False

        if root is None:
            return True
        return each_same(root.left, root.right)
