# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        def reserveListNode(head):
            new = None
            while head is not None:
                temp = head
                head = head.next
                temp.next = new
                new = temp
            return new
        if head is None or head.next is None:
            return True
        fast = slow = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        if fast is not None:
            slow = slow.next
        slow = reserveListNode(slow)
        while slow is not None:
            if slow.val != head.val:
                return False
            slow = slow.next
            head = head.next
        return True
