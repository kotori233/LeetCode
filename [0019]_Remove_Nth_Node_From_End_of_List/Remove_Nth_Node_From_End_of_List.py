# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast = head
        for i in range(n + 1):
            try:
                fast = fast.next
            except AttributeError:
                return head.next
        slow = head
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
