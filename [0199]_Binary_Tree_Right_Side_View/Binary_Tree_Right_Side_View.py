# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if root is None:
            return res
        father = [root]
        while father:
            temp = []
            child = []
            for i in father:
                temp.append(i.val)
                if i.left is not None:
                    child.append(i.left)
                if i.right is not None:
                    child.append(i.right)
            res.append(temp[-1])
            father = child
        return res
