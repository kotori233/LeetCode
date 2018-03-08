class Solution(object):

    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n, res = len(s), 0
        queue = [(i, i) for i in range(n)]
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                queue.append((i, i + 1))
        while queue:
            left, right = queue.pop(0)
            res += 1
            if left - 1 > -1 and right + 1 < n and s[left - 1] == s[right + 1]:
                queue.append((left - 1, right + 1))
        return res
