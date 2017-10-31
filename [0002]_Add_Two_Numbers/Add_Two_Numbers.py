# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        pre1 = l1
        cur1 = pre1.next
        pre2 = l2
        cur2 = pre2.next
        carry = 0
        while 1:
            d1 = pre1.val if pre1 else 0
            d2 = pre2.val if pre2 else 0
            temp = d1 + d2 + carry
            carry = temp // 10
            pre1.val = temp % 10
            if cur2 is not None:
                pre2 = cur2
                cur2 = pre2.next
            else:
                pre2 = None
            if cur1 is not None:
                pre1 = cur1
                cur1 = pre1.next
            elif carry or pre2:
                pre1.next = ListNode(0)
                cur1 = pre1.next
                pre1 = cur1
                cur1 = pre1.next
            else:
                break
        return l1
