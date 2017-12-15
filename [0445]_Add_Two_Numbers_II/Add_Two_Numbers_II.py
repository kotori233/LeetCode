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
        stack1, stack2, res = [], [], ListNode(0)
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        while stack1 or stack2:
            if stack1:
                res.val += stack1.pop()
            if stack2:
                res.val += stack2.pop()
            head = ListNode(res.val // 10)
            res.val %= 10
            head.next = res
            res = head
        if res.val:
            return res
        return res.next
