# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        father, res = [root], [root.val * 1.0]
        while 1:
            child, vals = [], 0
            for i in father:
                if i.left is not None:
                    child.append(i.left)
                    vals += i.left.val
                if i.right is not None:
                    child.append(i.right)
                    vals += i.right.val
            if child == []:
                break
            res.append(1.0 * vals / len(child))
            father = child
        return res
