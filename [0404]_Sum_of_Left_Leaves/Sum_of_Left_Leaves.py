# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        father = [root]
        res = 0
        while 1:
            child = []
            for i in father:
                if i.left is not None:
                    if i.left.left is None and i.left.right is None:
                        res += i.left.val
                    else:
                        child.append(i.left)
                if i.right is not None:
                    child.append(i.right)
            if child == []:
                break
            father = child
        return res
