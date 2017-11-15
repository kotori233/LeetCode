# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def divide(head):
            if not head or not head.next:
                return head
            slow = head
            fast = head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            left = head
            right = slow.next
            slow.next = None
            left = divide(left)
            right = divide(right)
            head = conquer(left, right)
            return head

        def conquer(left, right):
            dummy = ListNode('#')
            cur = dummy
            while left and right:
                if left.val > right.val:
                    cur.next = right
                    right = right.next
                else:
                    cur.next = left
                    left = left.next
                cur = cur.next
            if not left:
                cur.next = right
            else:
                cur.next = left
            return dummy.next

        return divide(head)
