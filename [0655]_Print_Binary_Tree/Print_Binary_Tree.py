# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        def height(root):
            if not root:
                return 0
            return 1 + max(height(root.left), height(root.right))

        def setTree(root, level, pos):
            if not root:
                return
            res[level][pos] = str(root.val)
            step = 1 + w >> level + 2
            setTree(root.left, level + 1, pos - step)
            setTree(root.right, level + 1, pos + step)

        h = height(root)
        w = (1 << h) - 1
        res = [['' for i in range(w)] for j in range(h)]
        setTree(root, 0, w >> 1)
        return res
