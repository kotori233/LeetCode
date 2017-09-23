# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        father = [root]
        deep = 1
        while 1:
            child = []
            for i in father:
                if i is not None:
                    if i.left is None and i.right is None:
                        return deep
                    child.extend([i.left, i.right])
            father = child
            deep += 1
