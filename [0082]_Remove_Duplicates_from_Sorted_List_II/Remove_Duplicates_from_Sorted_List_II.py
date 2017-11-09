# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        new = ListNode('#')
        new.next = head
        slow = new
        normal = slow.next
        fast = ListNode('#')
        while normal:
            if fast is None:
                slow.next = fast
                break
            fast = normal.next
            if fast is None:
                slow.next = normal
                break
            if normal.val != fast.val:
                slow.next = normal
                slow = slow.next
                normal = slow.next
                continue
            while fast:
                if fast.val == normal.val:
                    fast = fast.next
                else:
                    normal = fast
                    break
        return new.next
