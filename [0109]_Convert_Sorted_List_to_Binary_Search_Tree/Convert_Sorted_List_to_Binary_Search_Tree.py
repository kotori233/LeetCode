# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        def create(ret):
            i = len(ret) // 2
            root = TreeNode(ret[i])
            try:
                root.left = create(ret[:i])
            except IndexError:
                pass
            try:
                root.right = create(ret[i + 1:])
            except IndexError:
                pass
            return root

        if head is None:
            return None
        ret = []
        while head:
            ret.append(head.val)
            head = head.next
        return create(ret)
