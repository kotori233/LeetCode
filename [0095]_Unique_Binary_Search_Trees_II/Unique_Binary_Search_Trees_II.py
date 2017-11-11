# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def dfs(start, end):
            if start > end:
                return [None]
            res = []
            for rootVal in range(start, end + 1):
                leftNode = dfs(start, rootVal - 1)
                rightNode = dfs(rootVal + 1, end)
                for i in leftNode:
                    for j in rightNode:
                        root = TreeNode(rootVal)
                        root.left = i
                        root.right = j
                        res.append(root)
            return res

        if n == 0:
            return []
        return dfs(1, n)
