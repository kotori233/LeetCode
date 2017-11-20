# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def deepcount(root):
            count = 0
            while root:
                root = root.left
                count += 1
            return count

        def nodecount(root):
            if root is None:
                return 0
            deepL = deepcount(root.left)
            deepR = deepcount(root.right)
            if deepL == deepR:
                return (1 << deepL) + nodecount(root.right)
            return (1 << deepR) + nodecount(root.left)

        return nodecount(root)
