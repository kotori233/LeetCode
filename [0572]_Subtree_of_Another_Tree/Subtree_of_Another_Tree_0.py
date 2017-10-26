# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        self.temp = ''

        def preorder(root):
            if root is None:
                self.temp += ',#'
            else:
                self.temp += ',' + str(root.val)
                preorder(root.left)
                preorder(root.right)

        preorder(s)
        ps = self.temp
        self.temp = ''
        preorder(t)
        pt = self.temp
        if pt in ps:
            return True
        return False
