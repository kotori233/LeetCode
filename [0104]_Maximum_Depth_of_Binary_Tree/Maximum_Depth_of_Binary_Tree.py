# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        deep = 1
        father = [root]
        while 1:
            child = []
            for i in father:
                if i.left is not None:
                    child.append(i.left)
                if i.right is not None:
                    child.append(i.right)
            if child == []:
                break
            father = child
            deep += 1
        return deep
