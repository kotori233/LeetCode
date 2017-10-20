# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def dfs(root, sum):
            if root is None:
                return 0
            res = 1 if root.val == sum else 0
            res += dfs(root.left, sum - root.val)
            res += dfs(root.right, sum - root.val)
            return res

        if root is None:
            return 0
        res = dfs(root, sum)
        res += self.pathSum(root.left, sum)
        res += self.pathSum(root.right, sum)
        return res
