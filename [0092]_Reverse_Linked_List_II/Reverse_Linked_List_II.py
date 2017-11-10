# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        new = ListNode('#')
        new.next = head
        cur = new
        for i in range(m - 1):
            cur = cur.next
        cur0 = cur
        cur1 = cur.next
        for i in range(n - m):
            front = cur0.next
            temp = cur1.next
            cur1.next = temp.next
            cur0.next = temp
            temp.next = front
        return new.next
