# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.sheet = set()

        def preorder(root):
            if root is None:
                return False
            if k - root.val in self.sheet:
                return True
            else:
                self.sheet.add(root.val)
            return preorder(root.left) or preorder(root.right)

        return preorder(root)
