# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.res = []

        def postorder(root):
            if root is None:
                return 0
            left = postorder(root.left)
            right = postorder(root.right)
            depth = max(left, right)
            if depth == len(self.res):
                self.res.append([root.val])
            else:
                self.res[depth].append(root.val)
            return depth + 1

        postorder(root)
        return self.res
