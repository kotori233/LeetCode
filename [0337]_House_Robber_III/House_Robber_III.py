# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def postorder(root):
            if root.left is not None:
                postorder(root.left)
            else:
                root.left = TreeNode([0, 0])
            if root.right is not None:
                postorder(root.right)
            else:
                root.right = TreeNode([0, 0])
            update(root)

        def update(root):
            m1 = root.left.val[0] + root.right.val[0]
            m2 = root.val + root.left.val[1] + root.right.val[1]
            root.val = [max(m1, m2), m1]

        if root is None:
            return 0
        postorder(root)
        return root.val[0]
