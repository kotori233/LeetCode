# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        ans = [[root.val]]
        father = [root]
        while 1:
            child = []
            for i in father:
                if i.left is not None:
                    child.append(i.left)
                if i.right is not None:
                    child.append(i.right)
            if child == []:
                break
            ans.insert(0, [i.val for i in child])
            father = child
        return ans
