# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        try:
            root = TreeNode(preorder[0])
        except IndexError:
            return None
        i = inorder.index(preorder[0])
        try:
            root.left = self.buildTree(preorder[1:i + 1], inorder[:i])
        except IndexError:
            pass
        try:
            root.right = self.buildTree(preorder[i + 1:], inorder[i + 1:])
        except IndexError:
            pass
        return root
