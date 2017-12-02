# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        odd, right, new_odd = head, head.next, head.next.next
        while new_odd:
            left, new_odd, new_even = odd.next, right.next, new_odd.next
            odd.next = new_odd
            new_odd.next = left
            right.next = new_even
            odd, right = new_odd, new_even
            new_odd = new_even.next if new_even else None
        return head
