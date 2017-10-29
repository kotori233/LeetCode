# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.first, self.second = root.val, -1

        def search(root):
            if root is not None:
                if self.second == -1 and root.val > self.first:
                    self.second = root.val
                elif self.first < root.val < self.second:
                    self.second = root.val
                search(root.left)
                search(root.right)

        search(root)
        return self.second
