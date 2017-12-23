# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        father = [root]
        while 1:
            child = []
            for node in father:
                if node.left:
                    child.append(node.left)
                if node.right:
                    child.append(node.right)
            if child == []:
                break
            father = child
        return father[0].val
