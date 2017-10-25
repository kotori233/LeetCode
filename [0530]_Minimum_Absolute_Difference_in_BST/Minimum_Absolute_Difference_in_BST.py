# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.mindiff, self.pre = None, None

        def update(val):
            if self.pre is None:
                self.pre = val
                return
            if self.mindiff is None:
                self.mindiff = val - self.pre
                self.pre = val
                return
            else:
                self.mindiff = min(val - self.pre, self.mindiff)
                self.pre = val

        while root:
            if root.left is None:
                update(root.val)
                root = root.right
            else:
                pred = root.left
                while pred.right and pred.right is not root:
                    pred = pred.right
                if pred.right is None:
                    pred.right = root
                    root = root.left
                else:
                    # pred.right = None
                    update(root.val)
                    root = root.right
        return self.mindiff
