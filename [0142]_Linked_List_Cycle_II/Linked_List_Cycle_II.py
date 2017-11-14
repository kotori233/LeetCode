# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head
        while 1:
            if fast is None or fast.next is None:
                return None
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if slow == head:
            return head
        slow = head
        while 1:
            slow = slow.next
            fast = fast.next
            if slow == fast:
                return slow
