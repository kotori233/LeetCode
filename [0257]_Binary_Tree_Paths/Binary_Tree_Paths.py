# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []
        father = [root]
        paths_f = [str(root.val)]
        paths = []
        while 1:
            child = []
            paths_c = []
            for i in range(len(father)):
                fl, fr = father[i].left, father[i].right
                if fl is not None:
                    child.append(fl)
                    paths_c.append(paths_f[i] + '->' + str(fl.val))
                if fr is not None:
                    child.append(fr)
                    paths_c.append(paths_f[i] + '->' + str(fr.val))
                if fl is None and fr is None:
                    paths.append(paths_f[i])
            if paths_c == []:
                break
            paths_f = paths_c
            father = child
        return paths
