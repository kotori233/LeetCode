# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.pre = None

        def inorder(root):
            if root.right is not None:
                inorder(root.right)
            update(root)
            if root.left is not None:
                inorder(root.left)

        def update(root):
            if self.pre is None:
                self.pre = root.val
                return
            root.val += self.pre
            self.pre = root.val

        if root is None:
            return root
        inorder(root)
        return root
