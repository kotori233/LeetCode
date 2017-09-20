# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        pre = head
        cur = head.next
        while cur is not None:
            if pre.val != cur.val:
                pre = cur
                cur = cur.next
                continue
            while cur.next is not None and cur.val == cur.next.val:
                cur = cur.next
            pre.next = cur.next
            cur = pre.next
        return head
