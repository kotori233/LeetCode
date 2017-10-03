# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        o = ListNode(0)
        o.next = head
        pre = o
        while 1:
            if pre is None:
                break
            cur = pre.next
            while cur is not None and cur.val == val:
                pre.next = cur.next
                cur = cur.next
            pre = pre.next
        return o.next
