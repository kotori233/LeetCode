# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        try:
            root = TreeNode(postorder[-1])
        except IndexError:
            return None
        i = inorder.index(postorder[-1])
        try:
            root.left = self.buildTree(inorder[:i], postorder[:i])
        except IndexError:
            pass
        try:
            root.right = self.buildTree(inorder[i + 1:], postorder[i:-1])
        except IndexError:
            pass
        return root
