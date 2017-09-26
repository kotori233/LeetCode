# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        len_a = len_b = 1
        temp_a, temp_b = headA, headB
        while temp_a is not None:
            temp_a = temp_a.next
            len_a += 1
        while temp_b is not None:
            temp_b = temp_b.next
            len_b += 1
        diff = len_a - len_b
        temp_a, temp_b = headA, headB
        if diff < 0:
            for i in range(- diff):
                temp_b = temp_b.next
        if diff > 0:
            for i in range(diff):
                temp_a = temp_a.next
        while 1:
            if temp_a == temp_b:
                return temp_a
            temp_a = temp_a.next
            temp_b = temp_b.next
