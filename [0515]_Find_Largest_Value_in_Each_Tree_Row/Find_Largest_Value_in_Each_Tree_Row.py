# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        father = [root]
        while 1:
            child, m = [], float('-inf')
            for node in father:
                if node.val > m:
                    m = node.val
                if node.left:
                    child.append(node.left)
                if node.right:
                    child.append(node.right)
            res.append(m)
            if not child:
                break
            father = child
        return res
