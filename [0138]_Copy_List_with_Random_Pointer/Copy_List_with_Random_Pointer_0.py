# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None


class Solution(object):

    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None:
            return None
        queue = [head]
        new = RandomListNode(head.label)
        sheet = {head: new}
        while queue:
            cur = queue.pop(0)
            if cur.next:
                if cur.next not in sheet:
                    sheet[cur.next] = RandomListNode(cur.next.label)
                    queue.append(cur.next)
                sheet[cur].next = sheet[cur.next]
            if cur.random:
                if cur.random not in sheet:
                    sheet[cur.random] = RandomListNode(cur.random.label)
                    queue.append(cur.random)
                sheet[cur].random = sheet[cur.random]
        return new
