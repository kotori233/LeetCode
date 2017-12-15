# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        def update(node):
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            pre, cur = node, node.right
            while cur.left:
                pre = cur
                cur = cur.left
            node.val = cur.val
            if pre == node:
                pre.right = cur.right
            else:
                pre.left = cur.right
            return node

        cur, pre = root, None
        while cur:
            if key == cur.val:
                break
            pre = cur
            if key > cur.val:
                cur = cur.right
            else:
                cur = cur.left
        if not cur:
            return root
        if not pre:
            return update(cur)
        if pre.left and pre.left.val == key:
            pre.left = update(cur)
        else:
            pre.right = update(cur)
        return root
