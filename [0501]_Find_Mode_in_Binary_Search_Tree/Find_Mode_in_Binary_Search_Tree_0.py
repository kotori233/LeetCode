# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res = []
        self.tempCount, self.maxCount, self.pretempVal = 0, 0, None

        def update(val):
            if val == self.pretempVal:
                self.tempCount += 1
            else:
                if self.pretempVal is not None:
                    if self.tempCount > self.maxCount:
                        self.maxCount = self.tempCount
                        self.res = [self.pretempVal]
                    elif self.tempCount == self.maxCount:
                        self.res.append(self.pretempVal)
                self.tempCount = 1
                self.pretempVal = val

        def inorder(root):
            if root.left is not None:
                inorder(root.left)
                root.left = None
            if root.left is None:
                update(root.val)
            if root.right is not None:
                inorder(root.right)

        if root is None:
            return []
        inorder(root)
        if self.tempCount > self.maxCount:
            return [self.pretempVal]
        if self.tempCount == self.maxCount:
            self.res.append(self.pretempVal)
        return self.res
