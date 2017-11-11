# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if root is None:
            return res
        father = [root]
        flag = 0
        while 1:
            child = []
            temp = []
            flag = 1 - flag
            for i in father:
                temp.append(i.val)
                if i.left is not None:
                    child.append(i.left)
                if i.right is not None:
                    child.append(i.right)
            if flag:
                res.append(temp)
            else:
                res.append(temp[::-1])
            if child == []:
                break
            father = child
        return res
