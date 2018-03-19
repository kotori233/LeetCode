# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.res = []

        def helper(root):
            if not root:
                return 0
            t = root.val + helper(root.left) + helper(root.right)
            self.res.append(t)
            return t

        if not root:
            return False
        helper(root)
        print(self.res)
        t = self.res.pop() / 2
        return t in self.res
