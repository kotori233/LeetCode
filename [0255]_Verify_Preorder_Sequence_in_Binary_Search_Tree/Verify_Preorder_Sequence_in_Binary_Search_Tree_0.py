class Solution(object):

    def verifyPreorder(self, preorder):
        """
        :type n: List[int]
        :rtype: bool
        """
        min_val = 0x80000000
        cur = -1
        for i in preorder:
            if i < min_val:
                return False
            while cur > -1 and preorder[cur] < i:
                min_val = preorder[cur]
                cur -= 1
            cur += 1
            preorder[cur] = i
        return True
