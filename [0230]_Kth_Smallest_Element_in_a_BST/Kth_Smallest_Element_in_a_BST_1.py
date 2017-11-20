# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        count = 0
        while root:
            if root.left is None:
                count += 1
                if count == k:
                    return root.val
                root = root.right
            else:
                pred = root.left
                while pred.right and pred.right is not root:
                    pred = pred.right
                if pred.right is None:
                    pred.right = root
                    root = root.left
                else:
                    count += 1
                    if count == k:
                        return root.val
                    root = root.right
