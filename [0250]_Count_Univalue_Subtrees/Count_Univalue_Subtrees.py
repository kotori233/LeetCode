# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count = 0

        def isunival(root):
            if root is None:
                return True
            left = isunival(root.left)
            right = isunival(root.right)
            if left and right:
                if root.left and root.val != root.left.val:
                    return False
                if root.right and root.val != root.right.val:
                    return False
                self.count += 1
                return True
            return False

        isunival(root)
        return self.count
