# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def reverseListNode(head):
            if head is None:
                return head
            dummy = ListNode('#')
            dummy.next = head
            cur = head.next
            while cur:
                head.next = cur.next
                cur.next = dummy.next
                dummy.next = cur
                cur = head.next
            return dummy.next

        if head is None:
            return head
        head = reverseListNode(head)
        cur = head
        carry = 1
        while cur and carry:
            temp = cur.val + carry
            cur.val = temp % 10
            carry = temp // 10
            pre = cur
            cur = cur.next
        if carry == 1:
            pre.next = ListNode(1)
        return reverseListNode(head)
