# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or k == 0:
            return head
        cur = head
        count = 1
        while cur.next:
            cur = cur.next
            count += 1
        cur.next = head
        k %= count
        for i in range(count - k):
            cur = cur.next
        head = cur.next
        cur.next = None
        return head
