# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0

        def dfs(root):
            if root is None:
                return (0, float('-inf'), float('inf'))
            left = dfs(root.left)
            right = dfs(root.right)
            if root.val > left[1] and root.val < right[2]:
                temp = left[0] + right[0] + 1
                self.res = max(temp, self.res)
                return (temp, max(root.val, right[1]), min(root.val, left[2]))
            return (0, float('-inf'), float('inf'))

        dfs(root)
        return self.res
