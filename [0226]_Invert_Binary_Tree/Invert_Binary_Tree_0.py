# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        father = [root]
        while 1:
            child = []
            for i in father:
                if i.left is not None or i.right is not None:
                    i.left, i.right = i.right, i.left
                    if i.left is not None:
                        child.append(i.left)
                    if i.right is not None:
                        child.append(i.right)
            if child == []:
                break
            father = child
        return root
