# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if root is None:
            return res
        queue = [(root, 0)]
        sheet = {}
        while queue:
            root, i = queue.pop(0)
            sheet[i] = sheet.get(i, []) + [root.val]
            if root.left is not None:
                queue.append((root.left, i - 1))
            if root.right is not None:
                queue.append((root.right, i + 1))
        for i in sorted(sheet.keys()):
            res.append(sheet[i])
        return res
