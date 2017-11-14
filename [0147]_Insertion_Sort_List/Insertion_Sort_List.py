# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        dummy = ListNode('#')
        dummy.next = head
        cur = head
        while cur.next:
            if cur.val > cur.next.val:
                pre = dummy
                while pre.next.val <= cur.next.val:
                    pre = pre.next
                temp = cur.next
                cur.next = cur.next.next
                temp.next = pre.next
                pre.next = temp
            else:
                cur = cur.next
        return dummy.next
