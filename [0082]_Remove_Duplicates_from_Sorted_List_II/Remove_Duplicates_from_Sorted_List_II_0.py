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
        new = ListNode('#')
        new.next = head
        pre = new
        cur = pre.next
        while cur and cur.next:
            if cur.val != cur.next.val:
                pre = pre.next
                cur = pre.next
            else:
                temp = cur.val
                while cur and cur.val == temp:
                    cur = cur.next
                pre.next = cur
        return new.next
