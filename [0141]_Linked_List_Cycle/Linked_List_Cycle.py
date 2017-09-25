# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        fast = slow = head
        while 1:
            try:
                slow = slow.next
                fast = fast.next.next
            except AttributeError:
                return False
            if slow == fast:
                return True
