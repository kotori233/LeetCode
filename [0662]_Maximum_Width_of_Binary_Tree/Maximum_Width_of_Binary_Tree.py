# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0
        father = [(root, 1)]
        while father:
            res = max(res, father[-1][1] - father[0][1] + 1)
            child = []
            for node, i in father:
                if node.left:
                    child.append((node.left, i * 2))
                if node.right:
                    child.append((node.right, i * 2 + 1))
            father = child
        return res
