# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing

    def connect(self, root):
        if root:
            if root.right and root.left:
                root.left.next = root.right
            if root.right:
                temp = root
                while temp.next:
                    if temp.next.left:
                        root.right.next = temp.next.left
                        break
                    elif temp.next.right:
                        root.right.next = temp.next.right
                        break
                    temp = temp.next
            elif root.left:
                temp = root
                while temp.next:
                    if temp.next.left:
                        root.left.next = temp.next.left
                        break
                    elif temp.next.right:
                        root.left.next = temp.next.right
                        break
                    temp = temp.next
            if root.right:
                self.connect(root.right)
            if root.left:
                self.connect(root.left)
