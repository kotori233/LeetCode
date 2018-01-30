# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        dummy = TreeNode('#')
        dummy.left = root
        father = [dummy]
        deep = 1
        while deep < d:
            child = []
            for node in father:
                if node.left:
                    child.append(node.left)
                if node.right:
                    child.append(node.right)
            father = child
            deep += 1
        for node in father:
            temp = TreeNode(v)
            temp.left = node.left
            node.left = temp
            temp = TreeNode(v)
            temp.right = node.right
            node.right = temp
        return dummy.left
