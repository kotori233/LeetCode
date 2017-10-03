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
        if head is None:
            return None
        while 1:
            if head is not None and head.val == val:
                head = head.next
            else:
                break
        pre = head
        while 1:
            if pre is None:
                break
            cur = pre.next
            while cur is not None and cur.val == val:
                pre.next = cur.next
                cur = cur.next
            pre = pre.next
        return head
