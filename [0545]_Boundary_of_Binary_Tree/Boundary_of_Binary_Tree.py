# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]

        # leaves
        leaves = []

        def preorder(root):
            if not root.left and not root.right:
                leaves.append(root)
            if root.left:
                preorder(root.left)
            if root.right:
                preorder(root.right)

        preorder(root)

        # left
        left = []
        node = root.left
        while node and node != leaves[0]:
            left.append(node.val)
            if node.left:
                node = node.left
            else:
                node = node.right

        # right
        right = []
        node = root.right
        while node and node != leaves[-1]:
            right.append(node.val)
            if node.right:
                node = node.right
            else:
                node = node.left

        return [root.val] + left + [node.val for node in leaves] + right[::-1]
