# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        ret = []
        while head is not None:
            ret.insert(0, head.val)
            head = head.next
        head = ListNode(0)
        pre = head
        for i in range(len(ret)):
            pre.next = ListNode(ret[i])
            pre = pre.next
        return head.next
