# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def get_deep(tree):
            if tree is None:
                return 0
            left_deep = get_deep(tree.left)
            if left_deep < 0:
                return -1
            right_deep = get_deep(tree.right)
            if right_deep < 0:
                return -1
            deep = abs(left_deep - right_deep)
            if deep > 1:
                return -1
            return max(left_deep, right_deep) + 1

        if get_deep(root) == -1:
            return False
        return True
