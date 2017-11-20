# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.count = 0

        def inorder(root):
            if root.left is not None:
                temp = inorder(root.left)
                if temp is not None:
                    return temp
            self.count += 1
            if self.count == k:
                return root.val
            if root.right is not None:
                temp = inorder(root.right)
                if temp is not None:
                    return temp

        return inorder(root)
