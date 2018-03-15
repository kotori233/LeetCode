# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict


class Solution(object):

    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        self.sheet = defaultdict(list)

        def pattern(root):
            if not root:
                return '#'
            p = '%s(%s,%s)' % (root.val, pattern(
                root.left), pattern(root.right))
            self.sheet[p].append(root)
            return p

        pattern(root)
        return [self.sheet[p][0] for p in self.sheet if len(self.sheet[p]) > 1]
