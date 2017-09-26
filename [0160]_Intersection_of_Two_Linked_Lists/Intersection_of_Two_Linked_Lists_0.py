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
        temp_a, temp_b = headA, headB
        while 1:
            if temp_a == temp_b:
                break
            temp_a = temp_a.next
            temp_b = temp_b.next
            if temp_a is None and temp_b is None:
                break
            if temp_a is None:
                temp_a = headB
            if temp_b is None:
                temp_b = headA
        return temp_a
