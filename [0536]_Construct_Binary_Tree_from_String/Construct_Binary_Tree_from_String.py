# Definition for a binary tree node.
# class TreeNode(object):
#
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        if s == '':
            return None
        stack, i, n = [], 0, len(s)
        while i < n:
            if s[i] == '(':
                i += 1
            elif s[i] == ')':
                stack.pop()
                i += 1
            elif s[i].isdigit() or s[i] == '-':
                start = i
                i += 1
                while i < n and s[i].isdigit():
                    i += 1
                node = TreeNode(int(s[start:i]))
                if stack:
                    t = stack[-1]
                    if not t.left:
                        t.left = node
                    else:
                        t.right = node
                stack.append(node)
        return stack[-1]
