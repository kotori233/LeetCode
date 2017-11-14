# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None


class Solution(object):

    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        def dfs(node, sheet):
            if node is None:
                return None
            if node in sheet:
                return sheet[node]
            new = RandomListNode(node.label)
            sheet[node] = new
            new.next = dfs(node.next, sheet)
            new.random = dfs(node.random, sheet)
            return new

        return dfs(head, {})
