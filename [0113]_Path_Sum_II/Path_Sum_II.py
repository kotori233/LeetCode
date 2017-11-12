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
        :rtype: List[List[int]]
        """
        self.res = []

        def dfs(root, subres, subsum):
            subres0 = subres + [root.val]
            subsum0 = subsum + root.val
            if root.left is None and root.right is None:
                if subsum0 == sum:
                    self.res.append(subres0)
                return
            if root.left is not None:
                dfs(root.left, subres0, subsum0)
            if root.right is not None:
                dfs(root.right, subres0, subsum0)

        if root is None:
            return self.res
        dfs(root, [], 0)
        return self.res
