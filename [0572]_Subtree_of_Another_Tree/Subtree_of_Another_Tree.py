# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def preorder(root):
            if root.val == t.val and isSame(root, t):
                return True
            if root.left is not None:
                if preorder(root.left):
                    return True
            if root.right is not None:
                if preorder(root.right):
                    return True

        def isSame(p, q):
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            if p.val != q.val:
                return False
            if not isSame(p.left, q.left):
                return False
            if not isSame(p.right, q.right):
                return False
            return True

        if preorder(s) is None:
            return False
        return True
