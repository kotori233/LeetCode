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
        if head is None or head.next is None:
            return True
        ret = []
        while head is not None:
            ret.append(head.val)
            head = head.next
        if ret != ret[::-1]:
            return False
        return True
