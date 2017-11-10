# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if root is None:
            return res
        while root:
            if root.left is None:
                res.append(root.val)
                root = root.right
            else:
                pred = root.left
                while pred.right and pred.right is not root:
                    pred = pred.right
                if pred.right is None:
                    pred.right = root
                    root = root.left
                else:
                    res.append(root.val)
                    root = root.right
        return res
