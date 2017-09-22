# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        father = [root]
        while 1:
            child = []
            value = []
            for i in father:
                if i is not None:
                    child.extend([i.left, i.right])
                    if i.left is None:
                        value.append(None)
                    else:
                        value.append(i.left.val)
                    if i.right is None:
                        value.append(None)
                    else:
                        value.append(i.right.val)
            if value != value[::-1]:
                return False
            if value == [None] * len(value):
                return True
            father = child
