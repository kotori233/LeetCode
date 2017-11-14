# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        while root:
            res.append(root.val)
            if not root.left:
                root = root.right
            else:
                pred = root.left
                while pred.right and pred.right is not root.right:
                    pred = pred.right
                if not pred.right:
                    pred.right = root.right
                    root = root.left
                else:
                    root = root.right
        return res
