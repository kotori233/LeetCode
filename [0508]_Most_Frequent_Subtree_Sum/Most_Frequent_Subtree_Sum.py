# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res = []
        self.sheet = {}
        self.m = 0

        def postorder(root):
            if root.left:
                postorder(root.left)
            if root.right:
                postorder(root.right)
            if root.left:
                root.val += root.left.val
            if root.right:
                root.val += root.right.val
            temp = self.sheet.get(root.val, 0) + 1
            self.sheet[root.val] = temp
            if temp == self.m:
                self.res.append(root.val)
            elif temp > self.m:
                self.res = [root.val]
                self.m = temp

        if not root:
            return self.res
        postorder(root)
        return self.res
